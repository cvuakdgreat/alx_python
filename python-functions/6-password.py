def validate_password(password):
    if ' ' in password:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    if len(password) < 8:
        return False

    return True
