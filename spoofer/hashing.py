import hashlib

def calculate_hash(image_data: bytes, hash_algorithm: str = "sha512") -> str:
    """Calculate the hash of the given image data."""
    hash_obj = hashlib.new(hash_algorithm)
    hash_obj.update(image_data)
    return hash_obj.hexdigest()
