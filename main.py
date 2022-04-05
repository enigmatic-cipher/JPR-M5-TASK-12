"""
Given an array of numbers as input, print the sum of the digits of each number in
the array.
Input-> {10,25,456,67}
Output-> 1,7,15,13
"""

def sum_of_digit(n):
  for i in range(0,len(n)):
    sum = 0
    num = n[i]
    num_1 = str(num)
    for digit in num_1:
      sum = sum + int(digit)
    print(sum)
n = [10,25,456,67]
sum_of_digit(n)
    