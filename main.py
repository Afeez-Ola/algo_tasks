# def check_if_symmetric(word):
#     word = word.lower()
#     reversed_word = word[::-1]
#     print(word)
#     print(reversed_word)
#     if word == reversed_word:
#         return True
#     else:
#         return False

# word = input("Enter a word: ")
# print(check_if_symmetric(word))


def convert_to_numbers(string):
    alphabets = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    output_array = []
    for char in string:
        output_array.append(alphabets.index(char))
    return output_array

print(convert_to_numbers("a cat"))

