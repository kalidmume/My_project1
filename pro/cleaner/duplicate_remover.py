import os, hashlib

def remove_duplicates(folder):
    seen = {}
    removed = 0

    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            hash_value = hash_file(file_path)

            if hash_value in seen:
                os.remove(file_path)
                removed += 1
            else:
                seen[hash_value] = file_path

    print(f"♻️ Removed {removed} duplicate files.")

def hash_file(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()