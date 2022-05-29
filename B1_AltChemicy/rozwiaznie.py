def split_compund_to_groups(word):
    curr_group = ""
    group_list = []
    for i in word:
        if i == 'C' and curr_group != "":
            group_list.append(curr_group)
            curr_group = ""
        
        curr_group += i

    # We need add the last group as groups are added when the next one is found
    group_list.append(curr_group)

    return group_list


def is_palindrome(seed):
    return seed == seed[::-1]


def get_max_palindrome_length(word_list):
    max_length = 0
    for word in word_list:
        palindrome_groups = split_compund_to_groups(word)
        if len(palindrome_groups) > max_length and is_palindrome(palindrome_groups):
            max_length = len(palindrome_groups)

    return max_length
    

def read_file_to_list(file_name):
    with open(file_name, "r") as file:
        return file.read().splitlines()


def compare_palindromes(pwr_file, uwr_file):
    pwr_list = read_file_to_list(pwr_file)
    uwr_list = read_file_to_list(uwr_file)

    max_pwr = get_max_palindrome_length(pwr_list)
    max_uwr = get_max_palindrome_length(uwr_list)

    return (max_pwr, max_uwr)
