import hashlib

def generate_password_hash(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest()
    hashed_password = f"sha1:{sha1_hash}"
    return hashed_password

password = input("Enter password:")
hashed_password = generate_password_hash(password)
print(hashed_password)
