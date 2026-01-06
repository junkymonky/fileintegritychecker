import hashlib
import json

def generate_hash(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

file_name = "testfile.txt"
file_hash = generate_hash(file_name)

data = {
    "filename":file_name,
    "hash":file_hash
}

with open("hash_store.json", "w") as f:
    json.dump(data, f)

print("Hash generated and stores")