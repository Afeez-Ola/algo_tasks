from day1 import check_if_symmetric

tests = [
  {
    'function': check_if_symmetric,
    'input': "racecar",
    'output': True
  },
  {
    'function': check_if_symmetric,
    'input': "Hello",
    'output': False
  }
]

num_successes = 0
num_failures = 0

for test in tests:
  function = test['function']
  test_input = test['input']
  desired_output = test['output']
  actual_output = function(test_input)
  
  if actual_output == desired_output:
    num_successes +=1
  else:
    num_failures +=1
    function_name = function.__name__
    print('')
    print(f'{function_name} failed on input {test_input}')
    print(f"\tActual Ouput: {actual_output}")
    print(f'\tDesired Output: {desired_output}')
    
print(f'Testing complete: {num_successes} successes and {num_failures} failures.')
    