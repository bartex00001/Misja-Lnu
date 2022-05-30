def decrypt_character(encrypted_character):
    return chr(int(encrypted_character, 2))


def decrypt_message(encrypted_message, num_of_characters):
    decrypt_message = ""
    for i in range(num_of_characters):
        decrypt_message += decrypt_character(encrypted_message[i * 8: (i + 1) * 8])

    return decrypt_message


def generate_answer_from_message(encrypted_message):
    num_of_characters = len(encrypted_message) // 8
    answer = decrypt_message(encrypted_message, num_of_characters)

    return answer


def get_message_from_file(fileName):
    with open(fileName, 'r') as file:
        return file.read()


def decrypt_punchcard(file_name):
    encrypted_message = get_message_from_file(file_name)

    answer = generate_answer_from_message(encrypted_message)
    return answer
