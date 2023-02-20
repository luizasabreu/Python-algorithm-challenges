# Middle letter
# Write a function named mid that takes a string as its parameter. 
# Your function should extract and return the middle letter. 
# If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(word):
    word_size = len(word)
    if word_size %2 == 0:
        return "" 
    middle = int(word_size/2)
    return word[middle]



print(mid("aaaa"))
