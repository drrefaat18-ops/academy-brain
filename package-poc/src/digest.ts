// Portable digest kernel — harvested technique from D:\vault\Dr mahmoud MVP's
// src/server/first-route/source-digest.ts. Deterministic, no LLM calls.

export type SourceSpan = { start: number; end: number; text: string };

export type SourceDigest = {
  headings: string[];
  keyTerms: string[];
  definitions: { term: string; text: string; span: SourceSpan }[];
  coreFacts: string[];
  numbers: string[];
  sourceLength: number;
};

const HEADING_RE = /^#{1,6}\s+(.+)$/gm;
const DEFINITION_RE = /^([A-Z][A-Za-z0-9]*(?: [A-Za-z0-9]+){0,5})\s+(?:is|are|means|refers to)\s+([^.\n]{5,200})\./gm;
const NUMBER_RE = /\b\d+(?:\.\d+)?\s?(?:%|percent|mm|cm|m|kg|g|s|sec|seconds|min|minutes|V|volts?)\b/g;

function stripFences(text: string): string {
  return text.replace(/```[\s\S]*?```/g, "");
}

export function buildDigest(rawText: string): SourceDigest {
  const text = stripFences(rawText);

  const headings: string[] = [];
  for (const m of text.matchAll(HEADING_RE)) headings.push(m[1].trim());

  const definitions: SourceDigest["definitions"] = [];
  for (const m of text.matchAll(DEFINITION_RE)) {
    if (/^not\b/i.test(m[2])) continue;
    definitions.push({
      term: m[1].trim(),
      text: m[2].trim(),
      span: { start: m.index ?? 0, end: (m.index ?? 0) + m[0].length, text: m[0] },
    });
  }

  const numbers = Array.from(new Set(Array.from(text.matchAll(NUMBER_RE)).map((m) => m[0])));

  // Core facts: sentences that carry a number or a defined term — same
  // heuristic the MVP uses to separate "content" from prose filler.
  const sentences = text.split(/(?<=[.!?])\s+/).map((s) => s.trim()).filter(Boolean);
  const termSet = new Set(definitions.map((d) => d.term.toLowerCase()));
  const coreFacts = sentences.filter(
    (s) => NUMBER_RE.test(s) || [...termSet].some((t) => s.toLowerCase().includes(t)),
  );
  NUMBER_RE.lastIndex = 0;

  const keyTerms = Array.from(new Set(definitions.map((d) => d.term)));

  return {
    headings,
    keyTerms,
    definitions,
    coreFacts,
    numbers,
    sourceLength: text.length,
  };
}
