// Self-check for receipt.ts's state machine and invalidation logic.
// Run: npm run demo:receipt

import assert from "node:assert";
import { fingerprintBytes } from "./fingerprint";
import { newReceipt, recordApproval, lock, checkInvalidation, recordFailure } from "./receipt";

const deps = { sourceHash: "s1", requirementsHash: "r1", identityHash: "i1" };
const artifact = fingerprintBytes(Buffer.from("pdf-bytes-v1"));

let r = newReceipt("L1-s1");
assert.strictEqual(r.status, "PENDING");

r = recordApproval(r, artifact, 26, deps, "owner", "2026-08-31");
assert.strictEqual(r.status, "APPROVED");
assert.throws(() => recordApproval(r, artifact, 26, deps, "owner", "2026-08-31"), /expected PENDING/);
assert.throws(() => recordFailure(r), /expected PENDING/);

r = lock(r);
assert.strictEqual(r.status, "LOCKED");

assert.throws(() => recordFailure(r), /cannot fail a LOCKED receipt/);
assert.throws(() => recordApproval(r, artifact, 26, deps, "owner", "2026-08-31"), /expected PENDING/);

// unchanged deps + unchanged artifact -> stays LOCKED
let stillLocked = checkInvalidation(r, deps, artifact);
assert.strictEqual(stillLocked.status, "LOCKED");

// source changed -> INVALIDATED
let invalidated = checkInvalidation(r, { ...deps, sourceHash: "s2" }, artifact);
assert.strictEqual(invalidated.status, "INVALIDATED");
assert.match(invalidated.invalidatedReason ?? "", /source changed/);

// artifact silently swapped for different bytes -> INVALIDATED (tamper detection)
const swapped = fingerprintBytes(Buffer.from("different-bytes"));
let tampered = checkInvalidation(r, deps, swapped);
assert.strictEqual(tampered.status, "INVALIDATED");
assert.match(tampered.invalidatedReason ?? "", /no longer matches/);

// malformed persisted receipts fail closed rather than remaining approved/locked
const missingBindings = { ...r, artifact: null, dependencies: null };
const invalidBindings = checkInvalidation(missingBindings, deps, artifact);
assert.strictEqual(invalidBindings.status, "INVALIDATED");
assert.match(invalidBindings.invalidatedReason ?? "", /missing recorded approval bindings/);

// INVALIDATED is terminal; repeated checks preserve the original cause
assert.strictEqual(checkInvalidation(invalidated, deps, artifact), invalidated);

const failed = recordFailure(newReceipt("L1-s2"));
assert.strictEqual(failed.status, "FAILED");
assert.throws(() => recordFailure(failed), /expected PENDING/);
assert.throws(() => recordApproval(failed, artifact, 26, deps, "owner", "2026-08-31"), /expected PENDING/);

// approval snapshots caller-owned inputs instead of retaining mutable aliases
const mutableArtifact = { ...artifact };
const mutableDependencies = { ...deps };
const snapshotted = recordApproval(
  newReceipt("L1-s3"),
  mutableArtifact,
  26,
  mutableDependencies,
  "owner",
  "2026-08-31",
);
mutableArtifact.sha256 = "rewritten";
mutableDependencies.sourceHash = "rewritten";
assert.strictEqual(snapshotted.artifact?.sha256, artifact.sha256);
assert.strictEqual(snapshotted.dependencies?.sourceHash, deps.sourceHash);

// cannot lock a receipt that was never approved
assert.throws(() => lock(newReceipt("L2-s1")), /expected APPROVED/);

console.log("receipt.ts self-check: all assertions passed");
