import hashlib
import json

def generate_hash(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

with open("hash_store.json", "r") as f:
    stored_data = json.load(f)

current_hash = generate_hash(stored_data["filename"])

if current_hash == stored_data["hash"]:
    print("file is safe. No changes detected")

else:
    print("Warning!! file integrity compromised")