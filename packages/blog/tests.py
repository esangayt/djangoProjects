import hashlib
def generate_unique_token(device_id, company_id):
    # Concatenating the device ID and company ID
    string_to_hash = f"{device_id}_{company_id}"
    # Applying the SHA-1 algorithm
    hashed_string = hashlib.sha1(string_to_hash.encode()).hexdigest()
    return hashed_string
# Example usage
device_id = "59844"
company_id = "6835"
token = generate_unique_token(device_id, company_id)
print(token)