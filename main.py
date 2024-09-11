# import unittest
# def check_if_symmetric(word):
#     word = word.lower()
#     reversed_word = word[::-1]
#     # print(word)
#     # print(reversed_word)
#     if word == reversed_word:
#         return True
#     else:
#         return False

# # word = input("Enter a word: ")
# # print(check_if_symmetric(word))

# class TestSymmetryChecker(unittest.TestCase):
#   def not_palindrome(self):
#     self.assertFalse(check_if_symmetric("hello"))
  
#   def not_palindrome(self):
#     self.assertTrue(check_if_symmetric("madam"))
    
#   def test_mixed_case_palindrome(self):
#     self.assertTrue(check_if_symmetric("RaceCar"))
  
#   def test_empty_string(self):
#     self.assertTrue(check_if_symmetric(""))
    
#   def test_single_character_string(self):
#     self.assertTrue(check_if_symmetric("a"))
  
# if __name__ == "__main__":
#   unittest.main()


def convert_to_numbers(string):
    alphabets = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    output_array = []
    for char in string:
      if char not in alphabets:
        raise ValueError(f"Character {char} not in English alphabets!, try again with a valid English alphabet.")
      output_array.append(alphabets.index(char))
    return output_array

print(convert_to_numbers(""))


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

# def count_characters(string):
#   string = string.lower()
#   char_count = 0
#   char_dict= {}
#   for char in string:
#     if char in char_dict:
#       char_dict[char] += 1
#     else:
#       char_dict[char] = 1
#   return char_dict
  
# print(count_characters("A Cat"))



# def is_prime(N):
#   isPrime = False
#   if N % 2 == 0 or N % 3 == 0:
#     isPrime = False
#   elif (N == 2 or N == 3) or N >= 1:
#     isPrime = True 
#   return isPrime

# print(is_prime(17))
  