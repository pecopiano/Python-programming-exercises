# Question 15
# Level 2
# 
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa
# with a given digit as the value of a.

# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
# 

# Function: (taking the assignment a bit further!)
#	1 - Ask a digit
#	2 - Ask how many time it should be added (2--> a + aa / 4--> a + aa + aaa + aaaa)

# Ask the user a digit, and how many times it should be repeated then added to the other repetitions

def conv(digit, repeats):
        start = range(1,repeats+1)
        sequence = []
        count = 0
        for p in start: # Create a list of integers of the digit repeated p times 
                sequence.append(int(str(digit) * p))
        for p in sequence: # Add the resulting values
               count = count + p
        return count

digit = int(raw_input("digit? "))
repeats = int(raw_input("repeats? "))

print conv(digit,repeats)

# Book's Solution:
# a = raw_input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print n1+n2+n3+n4
