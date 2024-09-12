
def binary_to_decimal(string):
  decimal_value = 0
  binary_list = [int(num) for num in string]
  for i,num in enumerate(binary_list[::-1]):
    index = (len(binary_list) - i - 1)
    power_value = (2**index)
    decimal_value = power_value * num
    print(power_value)
  return decimal_value

if __name__ == "__main__":
  # string = input("Kindly enter a binary number: ")
  print(binary_to_decimal("11010"))
  
  