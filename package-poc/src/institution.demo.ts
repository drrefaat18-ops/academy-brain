// Self-check: the derived asset-ref regex must behave identically to
// academy-brain's hardcoded one (course.yaml / check_assets.py:58), and a
// second, unrelated institution profile must work with zero code changes —
// that's the proof TechnoSquare is no longer special-cased.
// Run: npm run demo:institution

import assert from "node:assert";
import { buildAssetRefPattern, TECHNOSQUARE_PROFILE, InstitutionProfile } from "./institution";

// The literal regex currently hardcoded in course.yaml's asset_discovery
// and duplicated in scripts/swarm/check_assets.py:58.
const HARDCODED_ACADEMY_BRAIN_REGEX =
  /`((?:img|tata|technosquare)[A-Za-z0-9_.\-]*\.(?:png|gif|jpg|jpeg))`/;

const derived = buildAssetRefPattern(TECHNOSQUARE_PROFILE);

assert.strictEqual(derived.source, HARDCODED_ACADEMY_BRAIN_REGEX.source);
assert.strictEqual(derived.flags, HARDCODED_ACADEMY_BRAIN_REGEX.flags);

assert.throws(
  () =>
    buildAssetRefPattern({
      ...TECHNOSQUARE_PROFILE,
      assetPrefixes: ["img", ""],
    }),
  /non-empty/,
  "an empty asset prefix must not broaden matching to every valid-looking filename",
);

const samples = [
  "`img-20-microbit-front.png`",
  "`tataWave.gif`",
  "`technosquareLogo.jpg`",
  "`unrelatedbrand-asset.png`", // must NOT match — proves the alternation is scoped, not wildcard
];

for (const s of samples) {
  const expected = HARDCODED_ACADEMY_BRAIN_REGEX.test(s);
  const actual = derived.test(s);
  assert.strictEqual(actual, expected, `mismatch for ${s}: derived=${actual} hardcoded=${expected}`);
}

const punctuationPrefix = "brand`.*+?^${}()|[]\\";
const punctuationRegex = buildAssetRefPattern({
  ...TECHNOSQUARE_PROFILE,
  assetPrefixes: [punctuationPrefix],
});
assert.ok(punctuationRegex.test(`\`${punctuationPrefix}-asset.png\``));
assert.ok(!punctuationRegex.test("`brand-anything.png`"));

// A second institution, invented on the spot, with no code changes.
const ministryOfEducation: InstitutionProfile = {
  id: "moe-eg",
  displayName: "Ministry of Education Robotics Track",
  language: "ar",
  assetPrefixes: ["moe", "wizara"],
  palette: { primary: "#1B5E20", secondary: "#FFFFFF" },
  mascot: null,
  prohibitedContent: ["brand logos other than MoE crest"],
};

const moeRegex = buildAssetRefPattern(ministryOfEducation);
assert.ok(moeRegex.test("`moe-slide12.png`"));
assert.ok(!moeRegex.test("`technosquareLogo.jpg`")); // TechnoSquare's own prefix must not leak into another institution's pattern

console.log("institution.ts self-check: all assertions passed");
