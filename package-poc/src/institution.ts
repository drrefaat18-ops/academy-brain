// Institution profile — the fix for academy-brain's hardcoded-brand problem
// (course.yaml: name "TechnoSquare micro:bit", asset_ref_pattern with
// "technosquare" baked into the regex; scripts/swarm/check_assets.py:58
// duplicates that same regex in code). This module makes brand/language/
// mascot/asset-naming runtime data instead of config-and-code constants,
// so TechnoSquare becomes one profile among many, not the only option.

export type InstitutionProfile = {
  id: string;
  displayName: string;
  language: "en" | "ar" | "en-ar";
  assetPrefixes: string[]; // e.g. ["img", "tata", "technosquare"]
  palette: { primary: string; secondary: string };
  mascot: string | null;
  prohibitedContent: string[];
};

// Builds the same shape of regex academy-brain currently hardcodes in two
// places (course.yaml's asset_discovery.asset_ref_pattern and
// scripts/swarm/check_assets.py:58's REF constant) — but derived from the
// profile's assetPrefixes instead of typed out per course.
export function buildAssetRefPattern(profile: InstitutionProfile): RegExp {
  if (profile.assetPrefixes.length === 0 || profile.assetPrefixes.some((prefix) => prefix.length === 0)) {
    throw new TypeError("assetPrefixes must contain only non-empty strings");
  }

  const alternation = profile.assetPrefixes.map(escapeRegex).join("|");
  return new RegExp(`\`((?:${alternation})[A-Za-z0-9_.\\-]*\\.(?:png|gif|jpg|jpeg))\``);
}

function escapeRegex(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

// Reference profile: TechnoSquare's current hardcoded config, expressed as
// data. This is the proof — the same asset-discovery behavior academy-brain
// has today, reproduced without a single course-specific string in code.
export const TECHNOSQUARE_PROFILE: InstitutionProfile = {
  id: "technosquare",
  displayName: "TechnoSquare micro:bit",
  language: "en",
  assetPrefixes: ["img", "tata", "technosquare"],
  palette: { primary: "#0A0A0A", secondary: "#D4AF37" }, // dark/gold, per L1-s1.production.yaml's brand-system notes
  mascot: "TATA",
  prohibitedContent: [],
};
