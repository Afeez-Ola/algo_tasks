
# def binary_to_decimal(string):
#   decimal_value = 0
#   binary_list = [int(num) for num in string]
#   for i,num in enumerate(binary_list[::-1]):
#     power_value = (2**i)
#     decimal_value += power_value * num
#   return decimal_value

# if __name__ == "__main__":
#   string = input("Kindly enter a binary number: ")
#   print(binary_to_decimal(string))



def hexadecimal_to_decimal(string):
  string = string.lower()
  decimal_value = 0
  position =0
  hexadecimal_list = []
  extracted_num_list = []
  extracted_alphabets_list = []
  decimal_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  alphabets_values = {"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
  reversed_string = list(reversed(string))
  for i, char in enumerate(reversed_string):
    index = len(string) - i -1
    if char in decimal_numbers:
      extracted_num_list.append(int(char))
    elif char in alphabets_values.keys():
      hexa_convert = 16**index
      print(char,index, hexa_convert)
      hexa_multiply = alphabets_values[char] * hexa_convert
      extracted_alphabets_list.append(hexa_multiply)
    hexadecimal_list = extracted_alphabets_list + extracted_num_list
    
      
  return decimal_value, extracted_num_list, extracted_alphabets_list, hexadecimal_list

if __name__ == "__main__":
  # string = input("Kindly enter a hexadecimal number: ")
  
  print(hexadecimal_to_decimal("3B07F"))
  
  