// Deterministic completeness check — harvested technique from the MVP's
// content-completeness.ts. Compares generated/bundled content against the
// digest; reports what source facts got dropped. Zero provider calls.

import { SourceDigest } from "./digest";

export type CompletenessReport = {
  totalFacts: number;
  presentFacts: number;
  missingFacts: string[];
  coveragePct: number;
};

function normalize(s: string): string {
  return s.toLowerCase().replace(/\s+/g, " ").trim();
}

export function checkCompleteness(digest: SourceDigest, generatedContent: string): CompletenessReport {
  const haystack = normalize(generatedContent);
  const missingFacts: string[] = [];

  for (const fact of digest.coreFacts) {
    const normFact = normalize(fact);
    // A fact "survives" if a meaningful chunk of its words appear together —
    // exact-substring is too strict once pedagogy content rephrases things.
    const words = normFact.split(" ").filter((w) => w.length > 3);
    const hitCount = words.filter((w) => haystack.includes(w)).length;
    const ratio = words.length ? hitCount / words.length : 1;
    if (ratio < 0.5) missingFacts.push(fact);
  }

  const presentFacts = digest.coreFacts.length - missingFacts.length;
  return {
    totalFacts: digest.coreFacts.length,
    presentFacts,
    missingFacts,
    coveragePct: digest.coreFacts.length ? Math.round((presentFacts / digest.coreFacts.length) * 100) : 100,
  };
}
