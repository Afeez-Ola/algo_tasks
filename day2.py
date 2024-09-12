
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
  decimal_value = 0
  position =0
  # hexadecimal_list = [int(num) for num in string]
  decimal_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  alphabets_values = ["a", "b", "c", "d", "e", "f"]
  for i, num in enumerate(reversed(string)):
    index = len(string) - i -1
    
    
  return decimal_value

if __name__ == "__main__":
  # string = input("Kindly enter a hexadecimal number: ")
  
  print(hexadecimal_to_decimal("3BB07F"))
  
  