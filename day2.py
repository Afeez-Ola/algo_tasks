
def binary_to_decimal(string):
  decimal_value = 0
  for char in range(len(string)-1,-1,-1):
    char = int(char)
    decimal_value+=2**char
  return decimal_value

if __name__ == "__main__":
  string = input("Kindly enter a binary number: ")
  print(binary_to_decimal(string))