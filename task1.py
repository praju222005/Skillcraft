def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

# Get user input
message = input("Enter message: ")
shift_value = int(input("Enter shift value: "))

# Encrypt and decrypt
encrypted_text = caesar_cipher(message, shift_value)
decrypted_text = caesar_cipher(encrypted_text, shift_value, encrypt=False)

# Display results
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")