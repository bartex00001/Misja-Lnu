def username_validate(username):
    allowed_characters = "qwertyuiopasdfghjklzxcvbnm1234567890"
    for character in username:
        if not character in allowed_characters:
            return False
    return True

print(username_validate(input()))
