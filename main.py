def check_if_symmetric(word):
    reversed_word = word[::-1]
    # print(word)
    # print(reversed_word)
    if word == reversed_word:
        return True
    else:
        return False

word = input("Enter a word: ")
print(check_if_symmetric(word))