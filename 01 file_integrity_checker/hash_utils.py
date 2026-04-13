import hashlib

def calculate_hash(file_path, algorithm="sha256"):
    hash_func = getattr(hashlib, algorithm)()

    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except:
        return None