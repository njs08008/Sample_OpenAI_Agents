import hashlib

def get_stable_id(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
