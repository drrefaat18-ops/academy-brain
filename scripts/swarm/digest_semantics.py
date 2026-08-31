"""Semantic layer over the extracted digest.

`digest_office.py` extracts slide text, notes, and images — it does not
analyze them. That is correct for extraction, but it means nothing
downstream knows which sentences actually carry the source's teachable
content, and nothing checks whether those survive into the bundle.

This module adds that layer. Technique ported from a prior app's
deterministic source-digest and content-completeness pair: identify the
definitions, terms, and core facts in the source, then check what share
of them still appear in a downstream artifact. Zero LLM cost, same as
the extraction it builds on — a fact silently dropped between digest and
bundle becomes visible instead of being something a reviewer has to
notice by eye.

Coverage is a signal, not a verdict: a bundle is *supposed* to transform
its source rather than echo it, so less than 100% is normal and expected.
What this catches is a specific named fact vanishing without a decision
having been made about it.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

# A definition is a line that opens with a short term and asserts what it
# is. Anchored to line start and capped at six words so descriptive
# sentences ("Our names are shown scrolling across...") do not read as
# definitions of their own subject.
_DEFINITION = re.compile(
    r"^([A-Z][A-Za-z0-9]*(?: [A-Za-z0-9]+){0,5})\s+(?:is|are|means|refers to)\s+([^.\n]{5,200})\.",
    re.MULTILINE,
)

_NUMBER = re.compile(
    r"\b\d+(?:\.\d+)?\s?(?:%|percent|mm|cm|m|kg|g|ms|s|sec|seconds|min|minutes|V|volts?)\b"
)

_FENCE = re.compile(r"```.*?```", re.DOTALL)

_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+|\n+")

_FRONTMATTER = re.compile(r"\A---\s*\n.*?\n---\s*(?:\n|\Z)", re.DOTALL)
_IMAGE_MANIFEST = re.compile(r"(?m)^## Images\s*$.*\Z", re.DOTALL)
_MARKDOWN_SCAFFOLD = re.compile(r"(?m)^(?:#{1,6}\s+.*|\*\*Speaker notes:\*\*)\s*$")

_LOGISTICS = re.compile(
    r"^(?:optionally\b|teacher:|model\b|open\b|download\b|encourage\b|"
    r"students?\b|you can (?:optionally\b|follow\b|share\b))",
    re.IGNORECASE,
)

_LEADING_ARTICLE = re.compile(r"^(?:An?|The|Our|Your|This|These|Those)\s+", re.IGNORECASE)

# "X is shown/used/placed..." is passive description, not definition. These
# participles are the exception: they introduce a genuine definition.
_DEFINITIONAL_PARTICIPLES = frozenset({"called", "known", "defined", "named"})

# Irregular past participles, which the "-ed" test above cannot catch.
_IRREGULAR_PARTICIPLES = frozenset(
    {
        "shown", "seen", "done", "given", "taken", "written", "made", "held",
        "built", "put", "sent", "kept", "left", "found", "run", "drawn",
        "shut", "set", "hidden", "chosen", "worn", "thrown",
    }
)

# A sentence with this many distinctive words states something, even when it
# names no defined term and carries no figure.
_MIN_CONTENT_WORDS = 4

# Words too generic to prove a fact survived — matching on these alone
# would mark almost anything present.
_STOPWORDS = frozenset(
    {
        "this", "that", "with", "from", "your", "then", "they", "them",
        "have", "will", "when", "what", "which", "used", "into", "there",
        "their", "about", "would", "could", "should", "does", "were", "been",
        "being", "where", "while", "also", "some", "each", "more", "very",
        "just", "students",
    }
)


def distinctive_words(text: str) -> list[str]:
    """Words specific enough to identify a fact, ignoring common filler."""
    return [
        w
        for w in re.findall(r"[a-z0-9]+", text.lower())
        if len(w) > 3 and w not in _STOPWORDS
    ]


def _is_content_candidate(sentence: str) -> bool:
    """Reject structural directions that cannot themselves be source facts."""
    return not (
        sentence.endswith("?")
        or "http://" in sentence.lower()
        or "https://" in sentence.lower()
        or _LOGISTICS.match(sentence)
    )


@dataclass
class Definition:
    term: str
    text: str
    start: int
    end: int


@dataclass
class Digest:
    definitions: list[Definition] = field(default_factory=list)
    key_terms: list[str] = field(default_factory=list)
    core_facts: list[str] = field(default_factory=list)
    numbers: list[str] = field(default_factory=list)
    source_length: int = 0


def build_digest(raw_text: str) -> Digest:
    """Identify definitions, terms, core facts, and figures in source text."""
    text = _FENCE.sub("", raw_text)
    text = _FRONTMATTER.sub("", text)
    text = _IMAGE_MANIFEST.sub("", text)
    text = _MARKDOWN_SCAFFOLD.sub("", text)

    definitions: list[Definition] = []
    for match in _DEFINITION.finditer(text):
        complement = match.group(2).strip()
        if complement.lower().startswith("not "):
            continue  # "X is not Y" is a contrast, not a definition
        complement_words = complement.split()
        first = complement_words[0].lower().rstrip(",")
        is_participle = first.endswith("ed") or first in _IRREGULAR_PARTICIPLES
        if is_participle and first not in _DEFINITIONAL_PARTICIPLES:
            continue  # "X is shown/placed/attached..." describes, not defines
        subject = _LEADING_ARTICLE.sub("", match.group(1).strip())
        term = subject
        definition_text = complement
        if first in _DEFINITIONAL_PARTICIPLES:
            # "X is called Y" defines Y, not the descriptive subject X.
            name = " ".join(complement_words[1:])
            name = re.sub(r"^as\s+", "", name, flags=re.IGNORECASE)
            term = _LEADING_ARTICLE.sub("", name.strip().rstrip(","))
            definition_text = subject
        if not term:
            continue
        definitions.append(
            Definition(term=term, text=definition_text, start=match.start(), end=match.end())
        )

    numbers = list(dict.fromkeys(_NUMBER.findall(text)))
    key_terms = list(dict.fromkeys(d.term for d in definitions))

    # A sentence carries content if it states a figure, speaks about a
    # defined term, or simply asserts enough substance to be teachable.
    # The last clause matters: a source with one definition still states
    # plenty of facts, and keying only on defined terms would miss them.
    lowered_terms = [t.lower() for t in key_terms]
    core_facts = [
        s
        for s in (raw.strip() for raw in _SENTENCE_SPLIT.split(text))
        if s
        and _is_content_candidate(s)
        and (
            _NUMBER.search(s)
            or any(t in s.lower() for t in lowered_terms)
            or len(distinctive_words(s)) >= _MIN_CONTENT_WORDS
        )
    ]

    return Digest(
        definitions=definitions,
        key_terms=key_terms,
        core_facts=core_facts,
        numbers=numbers,
        source_length=len(text),
    )


@dataclass
class CoverageReport:
    total_facts: int
    present_facts: int
    missing_facts: list[str]

    @property
    def coverage(self) -> float:
        if self.total_facts == 0:
            return 1.0
        return self.present_facts / self.total_facts


def check_coverage(digest: Digest, downstream_text: str, threshold: float = 0.5) -> CoverageReport:
    """Report which of the source's core facts are absent downstream.

    Matching is word-overlap rather than substring: a bundle legitimately
    rephrases what it carries, so an exact-text check would report
    everything missing. `threshold` is the share of a fact's distinctive
    words that must appear for it to count as carried through.
    """
    haystack_words = set(re.findall(r"[a-z0-9]+", downstream_text.lower()))
    missing: list[str] = []
    evaluated = 0

    for fact in digest.core_facts:
        words = list(dict.fromkeys(distinctive_words(fact)))
        if not words:
            continue  # nothing distinctive to match on; not evidence either way
        evaluated += 1
        hits = sum(1 for w in words if w in haystack_words)
        if hits / len(words) < threshold:
            missing.append(fact)

    return CoverageReport(
        total_facts=evaluated,
        present_facts=evaluated - len(missing),
        missing_facts=missing,
    )
