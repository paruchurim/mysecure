from cryptography.fernet import Fernet

# Generate a random key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Message to be encrypted
message = "Hello, this is a secret message."

# Encrypt the message
encrypted_message = cipher_suite.encrypt(message.encode())

# Decrypt the message
decrypted_message = cipher_suite.decrypt(encrypted_message).decode()

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
