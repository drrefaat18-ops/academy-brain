// Fingerprinting — the invariant behind academy-brain's lock discipline
// (00-contracts/pipeline-lessons.md section 7): every locked artifact is
// bound to SHA-256 + byte count + page count of the exact stored file, not
// a temporary generation result. This makes that check reusable outside a
// filesystem/git pipeline.

import { createHash } from "node:crypto";

export type ArtifactFingerprint = {
  sha256: string;
  byteCount: number;
};

export function fingerprintBytes(data: Buffer): ArtifactFingerprint {
  return {
    sha256: createHash("sha256").update(data).digest("hex"),
    byteCount: data.length,
  };
}

export function fingerprintsMatch(a: ArtifactFingerprint, b: ArtifactFingerprint): boolean {
  return a.sha256 === b.sha256 && a.byteCount === b.byteCount;
}
