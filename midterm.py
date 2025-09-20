import hashlib
from cryptography.fernet import Fernet

#get user input
choice = input("Enter s for string or f for file: ").strip().lower()

#read data
if choice == "s":
    text = input("enter text: ")
    data = text.encode()

elif choice == "f":
    filename = input("enter file path: ").strip()
    try:
        with open(filename, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        print("Error: file not found.")
        raise SystemExit

else:
    print("Invalid choice.")
    raise SystemExit

#hash data using SHA256
orig_hash = hashlib.sha256(data).hexdigest()

#encrypt input symmetric
#generate key
key = Fernet.generate_key()
fernet = Fernet(key)

#use fernet to encrypt message
encMessage = fernet.encrypt(data)

#decrypt message
decMessage = fernet.decrypt(encMessage)
dec_hash = hashlib.sha256(decMessage).hexdigest()

#check for integrity
print("Integrity check: ", "PASS" if dec_hash == orig_hash else "FAIL")

