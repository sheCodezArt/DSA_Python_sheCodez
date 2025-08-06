#!/usr/bin/env python3

#Given a list of strings and a character X, create a function that concatenates all strings containing X, but reverse every second string before concatenation.

my_list = ["hello", "very", "lost", "merry", "other", "pants", "hints", "tone"]

#char_X = input("Enter character: ")

char_X = "e"

def concat(a_list, x):
    final = ""
    count = 0
    for string in a_list:
        if x in string:
            if count % 2 == 1:
                final += string[::-1]
            else:
                final += string
            count += 1
    return final

print(concat(my_list, char_X))
