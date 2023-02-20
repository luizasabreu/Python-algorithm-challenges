# Consecutive zeros
# The goal of this challenge is to analyze a binary string consisting of only zeros and ones. 
# Your code should find the biggest number of consecutive zeros in the string. For example, given the string:
# "1001101000110"
# The biggest number of consecutive zeros is 3.
# Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. 
# Your function should return the number described above.

def consecutive_zeros(s):
    result = 0
    count = 0
    pivot = s[0]
    for i in s[1:]:
        if i == "0" and pivot == "0":
            count+=1
        if count > result:
            result = count
        pivot = i
    return result



print(consecutive_zeros("1001100000110"))