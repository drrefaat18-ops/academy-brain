// Step 1 proof: run the portable digest against academy-brain's real,
// already-locked L1-s1 session and check how much of it survives into the
// bundle. Read-only — does not touch academy-brain's own files.

import { readFileSync } from "node:fs";
import { join } from "node:path";
import { buildDigest } from "./digest";
import { checkCompleteness } from "./completeness";

const ROOT = "D:\\vault\\academy-brain";
const digestSource = readFileSync(join(ROOT, "10-digest", "L1-s1.md"), "utf8");
const blueprint = readFileSync(join(ROOT, "75-bundle", "L1-s1", "blueprint.md"), "utf8");

const digest = buildDigest(digestSource);
const report = checkCompleteness(digest, blueprint);

console.log("=== digest.ts on 10-digest/L1-s1.md ===");
console.log(`headings: ${digest.headings.length}`);
console.log(`keyTerms: ${digest.keyTerms.length} ->`, digest.keyTerms.slice(0, 10));
console.log(`coreFacts: ${digest.coreFacts.length}`);
console.log(`numbers found: ${digest.numbers.length} ->`, digest.numbers.slice(0, 10));

console.log("\n=== completeness.ts: digest facts vs 75-bundle/L1-s1/blueprint.md ===");
console.log(`coverage: ${report.presentFacts}/${report.totalFacts} (${report.coveragePct}%)`);
if (report.missingFacts.length) {
  console.log("missing facts (dropped between digest and bundle):");
  for (const f of report.missingFacts.slice(0, 10)) console.log(" -", f);
}
