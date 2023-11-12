def length(word_len):
    words = False
    if 3 <= len(word_len) <= 16:
        words = True
    return words


def contain_symbols(some_word):
    words = False
    if some_word.isalpha() or some_word.isalnum() or \
            " " in some_word or "_" in some_word or "-" in some_word:
        words = True
    return words


def redundant(redundant_word):
    words = False
    if " " not in redundant_word:
        words = True
    return words


usernames = input().split(", ")

for word in usernames:
    if contain_symbols(word) == True and length(word) == True and redundant(word) == True:
        print(word)
