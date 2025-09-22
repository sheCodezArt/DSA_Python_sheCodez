#!/usr/bin/env python3

def with_mod(x):
  if x % 2 == 0:
    return f"{x} is an even number"
  else:
    return f"{x} is an odd number"
  
def without_mod(a):
  count = 0
  while a > 1:
    count += 1
    a -= 2
  if a == 1:
    return f"{a+(2*count)} is an odd number"
  elif a == 0:
    return f"{a+(2*count)} is an even number"
  else:
    return "ERROR!!!"
 
num = 110

print(with_mod(num))
print(without_mod(num))
