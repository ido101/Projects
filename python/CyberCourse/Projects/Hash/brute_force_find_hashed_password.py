import hashlib
import itertools

# First way(Goes through 1-max_length passwords)
def brute_force_find_hashed_password(hashed_pass, charset, max_length):
    # Recursive function to generate all combinations of characters
    def generate_passwords(current_password):
        if len(current_password) > max_length:
            return False
        
        # Check if the current password matches the hashed password
        if hashlib.md5(current_password.encode()).hexdigest() == hashed_pass:
            print(f"Password found: {current_password}")
            return True
        
        # Try adding each character in the charset to the current password
        for char in charset:
            if generate_passwords(current_password + char):
                return True
        
        return False
    
    # Start generating passwords from an empty string
    generate_passwords("")


# Second way(Only tries passwords of length length)
def generate_passwords(charset, length):
   return itertools.product(charset, repeat=length) 

def calculate_md5_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

def decode_md5_hash(hashed_pass, charset, length):
    passwords = generate_passwords(charset, length)
    for password_tuple in passwords:
        password = ''.join(password_tuple)
        if calculate_md5_hash(password) == hashed_pass:
            print(f"Password found: {password}")
            return password
    print("Password not found.")
    return None

if __name__ == "__main__":
    hashed_pass = "3cc6520a6890b92fb55a6b3d657fd1f6"
    # Using both ways
    decode_md5_hash(hashed_pass, "0123456789", 6)
    brute_force_find_hashed_password(hashed_pass, "0123456789", 6)