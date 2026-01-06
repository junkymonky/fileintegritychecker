# File Integrity Checker

Simple Python scripts to generate and verify a SHA-256 hash for a file.

**Overview:**
- `generate_hash.py`: Computes a SHA-256 hash of `testfile.txt` and writes the filename and hash to `hash_store.json`.
- `verify_file.py`: Reads `hash_store.json`, recalculates the SHA-256 for the stored filename, and reports whether the file has changed.

**Requirements:**
- Python 3.8 or newer (uses the walrus operator `:=`). No external packages required.

**Usage:**
- Generate a hash (writes `hash_store.json`):

	```bash
	python3 generate_hash.py
	```

- Verify file integrity (reads `hash_store.json`):

	```bash
	python3 verify_file.py
	```

By default the scripts operate on `testfile.txt`. To hash or verify a different file, edit the `file_name` variable in `generate_hash.py` (and ensure `hash_store.json` points to that filename), or modify the scripts to accept a filename argument.

**Files:**
- `generate_hash.py` — compute and store the hash.
- `verify_file.py` — verify the stored hash against the current file.
- `hash_store.json` — JSON file storing `{"filename":..., "hash":...}` created by `generate_hash.py`.
- `testfile.txt` — example/test file included in the repo.

**Notes & Next Steps:**
- The scripts currently hard-code the filename. Consider updating them to accept a filename argument (via `argparse`) for more flexible usage.
- The project uses SHA-256; for higher-level workflows you may integrate timestamping or a secure key management system.

**License:**
This project is provided as-is; add your preferred license if you plan to reuse or distribute it.

