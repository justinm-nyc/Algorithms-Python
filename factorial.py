def findFactorialRecursive(number):
  if(number < 2):
    return 1
  return number * findFactorialRecursive(number-1)


def findFactorialIterative(number):
  answer = 1
  for i in range(2,number+1):
    answer = i * answer
  return answer

print(findFactorialRecursive(9))
print(findFactorialIterative(9))