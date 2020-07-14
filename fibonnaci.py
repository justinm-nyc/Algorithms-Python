# Given a number N return the index value of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

#For example: fibonacciRecursive(6) should return 8

def fibonacciRecursive(n):
  if(n == 0):
    return 0
  elif(n < 3):
    return 1
  return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)

def fibonacciIterative(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
    
  seqArray = [0,1]
  for i in range(2, n+1):
    seqArray.append(seqArray[i-1] + seqArray[i-2])
  return seqArray[n]
