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


# def convert_to_numbers(string):
#     alphabets = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     output_array = []
#     for char in string:
#         output_array.append(alphabets.index(char))
#     return output_array

# print(convert_to_numbers("a cat"))


# def convert_to_numbers(num_list):
#     alphabets = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     output_char_list = []
#     for num in num_list:
#         output_char_list.append(alphabets[num])
#     output_string = "".join(output_char_list)
#     return output_string

# print(convert_to_numbers([1,0,3,1,20]))


# def get_intersection(array1, array2):
#     intersect_array = []
#     for item in array1:
#         if item in array2 and item not in intersect_array:
#             intersect_array.append(item)
#     return intersect_array

# print(get_intersection(array1 = [1, 3,3, 5, 7, 9],array2 = [3, 6, 7, 10]))



# def get_union(array1, array2):
#     union_array = []
#     for i in array1:
#         if i not in union_array:
#             union_array.append(i)
#         for j in array2:
#             if j not in union_array:
#                 union_array.append(j)
            
#     return sorted(union_array)

# print(get_union(array1 = [1, 3,3, 5, 7, 9],array2 = [3, 6, 7, 10]))

def count_characters(string):
  char_count = 0
  char_array = []
  for char in string:
    char_array.append(char)
  return char_array
  
print(count_characters("A cat"))