#!/usr/bin/env python3

def sum_of_nums(x):
    total = 0
    for i in range(x + 1):
      total += i
    return total
    
# def seq_sum(a):
#   return a * (a + 1)

num = 10
print(sum_of_nums(num))
# print(seq_sum(num))