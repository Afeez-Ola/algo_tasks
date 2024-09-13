
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
  binary_list = []
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
      # print(char,index, hexa_convert)
      hexa_multiply = alphabets_values[char] * hexa_convert
      extracted_alphabets_list.append(hexa_multiply)
  binary_list = extracted_alphabets_list + extracted_num_list
  result = map_array_to_string_index(binary_list,string)
  return  result

  
def map_array_to_string_index(arr, string):

    string = string.lower()
    result = {}

    for num in arr:
        hex_str = format(num, 'x')

        # Find the index of the **first** occurrence of the **leftmost** character in hex_str that exists in string
        for i in range(len(hex_str)):
            if hex_str[i] in string:
                index = string.index(hex_str[i])
                result[num] = index
                break

    return result




    
      

if __name__ == "__main__":
  # string = input("Kindly enter a hexadecimal number: ")
  
  print(hexadecimal_to_decimal("3B07F"))
  
  