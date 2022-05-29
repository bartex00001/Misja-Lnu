from compare_results import compare_palindromes
import random

FILE_NAME_PWR = "pwr.txt"
FILE_NAME_UWR = "uwr.txt"
NUMBER_OF_RANDOM_TESTS = 10

SUCCESS_MESSAGE = ""
FAIL_MESSAGE = "Huh? To przecież niemożliwe!\nCzy twój program napewno działa poprawnie?"

ATOM_LIST = ['C', 'H', 'N', 'O', 'F']


def read_file_to_list(file_name):
    with open(file_name, "r") as file:
        return file.read().splitlines()


def is_palindrome(word):
    return word == word[::-1]


def get_max_palindrome_length(word_list):
    max_length = 0
    for word in word_list:
        if len(word) > max_length and is_palindrome(word):
            max_length = len(word)

    return max_length


def get_answer():
    pwr_list = read_file_to_list(FILE_NAME_PWR)
    uwr_list = read_file_to_list(FILE_NAME_UWR)

    max_pwr = get_max_palindrome_length(pwr_list)
    max_uwr = get_max_palindrome_length(uwr_list)

    return (max_pwr, max_uwr)


def random_test():
    setup_test()
    try:
        usr_answer = compare_palindromes(FILE_NAME_PWR, FILE_NAME_UWR)
        expected = get_answer()

        return usr_answer == expected
    except:
        return False


def setup_test():
    pwr_list = generate_palindrome_list()
    uwr_list = generate_palindrome_list()
    write_list_to_file(pwr_list, FILE_NAME_PWR)
    write_list_to_file(uwr_list, FILE_NAME_UWR)


def generate_palindrome_list():
    li = []
    list_length = random.randint(4, 100)

    for i in range(list_length):
        li.append(generate_random_word())

    return li


def generate_random_word():
    word = ""
    word_length = random.randint(2, 30)

    for i in range(word_length):
        word += random.choice(ATOM_LIST)

    # To make sure that at least some words are palindromes
    if random.randint(0, 1) == 0:
        word += word[::-1]

    return word


def write_list_to_file(list, file_name):
    with open(file_name, "w") as file:
        for item in list:
            file.write(item + "\n")


def test():
    for i in range(NUMBER_OF_RANDOM_TESTS):
        if not random_test():
            komunikat = FAIL_MESSAGE
            return False
    
    komunikat = SUCCESS_MESSAGE
    return True
