# Question 14
# Level 2
# 
# Question:
# Write a program that accepts a sentence
# and calculate the number of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

import re

test_string = "Hello World! WORLD And whatever the hell that MEANS"

split = ''.join(re.split(r'\W+', test_string))

upper = 0
lower = 0

for p in split:
    if p.isupper():
        upper += 1
    elif p.islower():
        lower += 1


print upper
print lower
