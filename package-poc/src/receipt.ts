// Receipt state machine — portable version of academy-brain's
// 90-receipts/*.production.yaml lock discipline (00-contracts/pipeline-lessons.md
// section 7) plus the MVP's self-invalidating approval pattern
// (source-pack-invalidation.ts: stale approvals die when their inputs change).
//
// Deterministic state only. No provider calls, no filesystem — the caller
// supplies fingerprints and dependency hashes; this module just enforces
// the transitions.

import { ArtifactFingerprint, fingerprintsMatch } from "./fingerprint";

export type ReceiptStatus = "PENDING" | "FAILED" | "APPROVED" | "LOCKED" | "INVALIDATED";

export type DependencyFingerprints = {
  sourceHash: string;
  requirementsHash: string;
  identityHash: string;
};

export type Receipt = {
  sessionId: string;
  status: ReceiptStatus;
  artifact: ArtifactFingerprint | null;
  pageCount: number | null;
  dependencies: DependencyFingerprints | null;
  approvedBy: string | null;
  approvedAt: string | null;
  invalidatedReason: string | null;
};

export function newReceipt(sessionId: string): Receipt {
  return {
    sessionId,
    status: "PENDING",
    artifact: null,
    pageCount: null,
    dependencies: null,
    approvedBy: null,
    approvedAt: null,
    invalidatedReason: null,
  };
}

export function recordFailure(receipt: Receipt): Receipt {
  if (receipt.status === "LOCKED") {
    throw new Error(`cannot fail a LOCKED receipt for ${receipt.sessionId}`);
  }
  if (receipt.status !== "PENDING") {
    throw new Error(`cannot fail ${receipt.sessionId}: status is ${receipt.status}, expected PENDING`);
  }
  return { ...receipt, status: "FAILED" };
}

// Owner visual approval is mandatory before lock — pipeline-lessons.md
// section 7. This function only records the approval; it does not lock.
export function recordApproval(
  receipt: Receipt,
  artifact: ArtifactFingerprint,
  pageCount: number,
  dependencies: DependencyFingerprints,
  approvedBy: string,
  approvedAt: string,
): Receipt {
  if (receipt.status !== "PENDING") {
    throw new Error(`cannot approve ${receipt.sessionId}: status is ${receipt.status}, expected PENDING`);
  }
  return {
    ...receipt,
    status: "APPROVED",
    artifact: { ...artifact },
    pageCount,
    dependencies: { ...dependencies },
    approvedBy,
    approvedAt,
    invalidatedReason: null,
  };
}

export function lock(receipt: Receipt): Receipt {
  if (receipt.status !== "APPROVED") {
    throw new Error(`cannot lock ${receipt.sessionId}: status is ${receipt.status}, expected APPROVED`);
  }
  return { ...receipt, status: "LOCKED" };
}

// Self-invalidation: if any dependency the approval was bound to has since
// changed, or the stored artifact no longer matches its recorded
// fingerprint, the approval (or lock) is no longer trustworthy and must be
// re-earned. Ported from the MVP's source-pack-invalidation.ts.
export function checkInvalidation(
  receipt: Receipt,
  currentDependencies: DependencyFingerprints,
  currentArtifact: ArtifactFingerprint,
): Receipt {
  if (receipt.status !== "APPROVED" && receipt.status !== "LOCKED") return receipt;
  if (!receipt.dependencies || !receipt.artifact) {
    return {
      ...receipt,
      status: "INVALIDATED",
      invalidatedReason: "missing recorded approval bindings",
    };
  }

  const reasons: string[] = [];
  if (receipt.dependencies.sourceHash !== currentDependencies.sourceHash) reasons.push("source changed");
  if (receipt.dependencies.requirementsHash !== currentDependencies.requirementsHash) reasons.push("requirements changed");
  if (receipt.dependencies.identityHash !== currentDependencies.identityHash) reasons.push("identity/brand changed");
  if (!fingerprintsMatch(receipt.artifact, currentArtifact)) reasons.push("stored artifact no longer matches its recorded fingerprint (tamper or silent replace)");

  if (reasons.length === 0) return receipt;

  return {
    ...receipt,
    status: "INVALIDATED",
    invalidatedReason: reasons.join("; "),
  };
}
