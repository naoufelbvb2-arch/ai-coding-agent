# Stage A verification commands and results

Run from the repository root in PowerShell. Python 3.14.4 was used. The scripts below are new documentation inventory/verification helpers; none imports or executes code from the supplied archive.

```powershell
python documentation_checkpoint/tools/archive_inventory.py
python documentation_checkpoint/tools/inspect_sources.py
python documentation_checkpoint/tools/archive_inventory.py --verify
python documentation_checkpoint/tools/verify_checkpoint.py
```

The first command is idempotent preservation: an existing archive file with different bytes is refused rather than overwritten. It initializes the file inventory; the second command enriches its classification and creates source-unit and section indices. For later custody checks, use `--verify` rather than regenerating the inventory.

Observed source checks: 195 preserved files, two complete ZIP CRC checks, three handoff SHA-256 matches, two FCA sidecar matches, 27 exact per-message SHA-256/length/bundle-presence matches, final freeze evidence in all ten RDMS bundles, 88 unique FCA base sections, seven appendices, and zero JSON parse failures across 179 inspected text artifacts. Results are recorded in [VERIFICATION_RESULTS.json](VERIFICATION_RESULTS.json).

Git setup used the user-supplied repository. Both `git ls-remote --symref <repository> HEAD` and `git ls-remote <repository>` returned exit code 0 with no refs. This established an accessible repository with no advertised history during inspection. Setup commands:

```powershell
git init -b docs/canonical-source-checkpoint
git remote add origin https://github.com/naoufelbvb2-arch/ai-coding-agent.git
```

Archive attributes disable Git text normalization. All original files, including cache/history files that would normally be ignored, are deliberately force-added for archival custody:

```powershell
git add .gitattributes .gitignore documentation_checkpoint
git add -f documentation_checkpoint/source_archive
python documentation_checkpoint/tools/verify_checkpoint.py --git-index
```

The index check compares the SHA-256 of each of the 195 staged Git blobs against the original file inventory; it also checks source-unit locators, the one-owner FCA allocation, all twelve interface IDs, local checkpoint report links, documentation branch/origin, and absence of a live canonical architecture directory. Whitespace checks should be restricted to new checkpoint reports/helpers, because the immutable archived originals may contain historical whitespace defects and must remain unchanged:

```powershell
git diff --cached --check -- .gitattributes .gitignore documentation_checkpoint/CHECKPOINT_REVIEW.md documentation_checkpoint/INTERFACE_REVIEW_PLAN.md documentation_checkpoint/UNRESOLVED_ISSUES.md documentation_checkpoint/VERIFICATION.md documentation_checkpoint/tools
git commit -m "docs: inventory authoritative architecture sources and propose layer ownership"
python documentation_checkpoint/tools/verify_checkpoint.py --git-head
git status --short --branch
```

The restricted whitespace check passed with no findings. The staged-blob check passed for all 195 originals with zero locator, ownership, interface-ID or local-link errors; its recorded result is in [VERIFICATION_GIT_INDEX.json](VERIFICATION_GIT_INDEX.json). The initial commit attempt failed because no Git author identity was configured. After the user supplied the email, repository-local author configuration used `naoufelbvb2-arch` and `naoufelbvb2@gmail.com`. Checkpoint commit `9ec210201123acac331738ab32607a74c456750d` was created successfully. **All 195 committed original-source hashes passed**, with zero verification errors; the observed result is in [VERIFICATION_GIT_HEAD.json](VERIFICATION_GIT_HEAD.json). The follow-up verification-record commit changes only checkpoint documentation and evidence.

These checks establish the checkpoint's inventory, locators and custody. They **do not** establish complete effective-law reconciliation, ratification of callable interface signatures, fault-tested runtime behavior, or consolidated architecture freeze. Historical test logs in the archive were inventoried as evidence and were not rerun. No branch was pushed and no main merge was performed at this checkpoint.
