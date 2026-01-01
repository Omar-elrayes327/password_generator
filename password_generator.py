import string
import secrets

def generate_password(length, upper, digits, symbols):
    chars = string.ascii_lowercase

    if upper:
        chars += string.ascii_uppercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    return ''.join(secrets.choice(chars) for _ in range(length))