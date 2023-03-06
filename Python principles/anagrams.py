# Anagrams
# Two strings are anagrams if you can make one from the other by rearranging the letters.
# Write a function named is_anagram that takes two strings as its parameters. 
# Your function should return True if the strings are anagrams, and False otherwise.
# For example, the call is_anagram("typhoon", "opython") should return True 
# while the call is_anagram("Alice", "Bob") should return False

def create_dict(word):
    result = {}
    for i in word:
        if i in result.keys():
            result[i] += 1
        else:
            result[i] = 1
    result = sorted(result.items())

    return result

def is_anagram(s1, s2):
    s1_dict = create_dict(s1)
    s2_dict = create_dict(s2)
    if s1_dict == s2_dict:
        return True
    return False

print(is_anagram("typhoon", "opython"))