#!/bin/python3

#enter number
n = int(input())

#odd case
if n % 2 == 1:
  print("Weird")
  
#even case
#range function do not incude stop value
elif n % 2 == 0 and n in range(2,6):
    print("Not Weird")
elif n % 2 == 0 and n in range(6,21):
    print("Weird")
elif n % 2 == 0 and n in range(21,101):
    print("Not Weird")
else:
    print("exit")
