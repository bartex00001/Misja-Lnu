from decrypt_punchcard import decrypt_punchcard
import random

FILE_NAME = "punchcard.txt"
NUMBER_OF_RANDOM_TESTS = 5

SUCCESS_MESSAGE = "Udało się!" # TODO: wymyśleć zakodowaną wiadomość
FAIL_MESSAGE = "Coś chyba jest nie tak, spróbuj jeszcze raz"

def generate_punchcard_message():
    len = random.randint(5, 50)
    punchcard_message = ""

    for i in range(len):
        punchcard_message += chr(random.randint(97, 122))

    return punchcard_message


def setup_task(punchcard_message):
    encrypted_message = convert_text_to_bin_ascii(punchcard_message)
    write_message_to_file(encrypted_message)


def convert_text_to_bin_ascii(text):
    return ["0{0:b}".format(ord(c)) for c in text]


def write_message_to_file(punchcard_message):
    with open(FILE_NAME, "w") as f:
        for i in punchcard_message:
            f.write(str(i))


def random_test():
    punchcard_message = generate_punchcard_message()
    setup_task(punchcard_message)

    try:
        answer = decrypt_punchcard(FILE_NAME)
        return answer == punchcard_message

    except:
        return False


def test():
    for i in range(NUMBER_OF_RANDOM_TESTS):
        if not random_test():
            komunikat = FAIL_MESSAGE
            return False

    komunikat = SUCCESS_MESSAGE
    return True
