from compare_results import compare_palindromes
import random

FILE_NAME_PWR = "pwr.txt"
FILE_NAME_UWR = "uwr.txt"
NUMBER_OF_RANDOM_TESTS = 10

SUCCESS_MESSAGE = "" # TODO: create succes message (relevant to task story)
FAIL_MESSAGE = "Huh? To przecież niemożliwe!\nCzy twój program napewno działa poprawnie?"

# List is staticly typed for simplicity.
# It can be easely generated at runtime.
ATOM_LIST = ['CHOH', 'CHH', 'CH', 'C', 'CHNHH', 'CFH']


def read_file_to_list(file_name):
    with open(file_name, "r") as file:
        return file.read().splitlines()


def convert_compound_to_seed(compound):
    seed = []
    curr_group = ""

    for i in compound:
        if i == 'C' and curr_group != "":
            seed.append(ATOM_LIST.index(curr_group))
            curr_group = ""

        curr_group += i
            
    # We need to check the last compound (no event triggers it)
    seed.append(ATOM_LIST.index(curr_group))
    return seed


def is_palindrome(seed):
    return seed == seed[::-1]


def get_max_palindrome_length(word_list):
    max_length = 0
    for word in word_list:
        seed = convert_compound_to_seed(word)
        if len(seed) > max_length and is_palindrome(seed):
            max_length = len(seed)

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
        li.append(generate_random_compound())

    return li


def generate_random_compound():
    seed = generate_compound_seed()
    compound = ""

    for i in seed:
        compound += ATOM_LIST[i]

    return compound


def generate_compound_seed():
    li = [random.randint(0, len(ATOM_LIST)-1) for i in range(random.randint(2, 20))]

    if random.randint(0, 1) == 0:
        li += li[::-1]

    return li


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
