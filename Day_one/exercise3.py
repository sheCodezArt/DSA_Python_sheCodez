#!/usr/bin/env python3

import re

#Create a function that accepts a password string and returns True if it meets: length 8+, contains uppercase, lowercase, digit, and special char; otherwise False.

def check_pwd(pwd):
    if len(pwd) < 8:
        return False
    if not any(c.isupper() for c in pwd):
        return False
    if not any(c.islower() for c in pwd):
        return False
    if not any(c.isdigit() for c in pwd):
        return False
    if not (re.search(r'[^a-zA-Z0-9\s]', pwd)):
        return False
    return True

my_pwd = "Strong_pa55w0rd"
print(check_pwd(my_pwd))
