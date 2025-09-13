#!/usr/bin/env python3

#Write a function that takes a positive integer N and returns the sum of all numbers less than N that are multiples of 3 or 5, but skip multiples of 7.

def multiples(n):
    if n < 0:
        return "Sorry, cannot accept negative numbers. Try again"
    else:
        result = 0
        for i in range(n):
            if i % 7 == 0:
                continue
            if i % 3 == 0 or i % 5 == 0:
                result += i
        return result

print(multiples(55))
