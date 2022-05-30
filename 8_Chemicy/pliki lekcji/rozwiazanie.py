
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
    

def compare_palindromes(pwr_file, uwr_file):
    pwr_list = read_file_to_list(pwr_file)
    uwr_list = read_file_to_list(uwr_file)

    maxPwr = get_max_palindrome_length(pwr_list)
    maxUwr = get_max_palindrome_length(uwr_list)

    return (maxPwr, maxUwr)