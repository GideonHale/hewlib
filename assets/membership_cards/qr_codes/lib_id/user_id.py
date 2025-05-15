import hashlib

BASE = 36  # Adjust this value as needed

def user_id(name, timestamp):
    first_char = "U"
    
    # Combine name and timestamp into a single string
    combined_string = f"{name}-{timestamp}"
    
    # Generate SHA-1 hash of the combined string
    hash_obj = hashlib.sha1(combined_string.encode())
    hash_hex = hash_obj.hexdigest()
    
    # Define the Base 62 alphabet (or adjust it based on the BASE variable)
    base62_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    base_chars = base62_chars[:BASE]
    
    # Convert the first 15 characters of the hash to an integer
    value = int(hash_hex[:15], 16)
    
    # Convert to the specified base
    base_code = ""
    while value > 0 and len(base_code) < 11:
        remainder = value % BASE
        base_code = base_chars[remainder] + base_code
        value //= BASE
    
    # Pad to ensure the code is exactly 11 characters (after "U")
    base_code = base_code.zfill(11)
    
    # Combine "U" with the rest of the base code
    return first_char + base_code
