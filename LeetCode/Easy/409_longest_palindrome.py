"""
Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
class Solution:
    def longestPalindrome(self, s: str) -> int: # "abccccdd" - "aabb" - "a" - "aaa" - "bananas"
        count_pairs = 0
        dictionary = {}
        for i in s:
            if i in dictionary.keys():
                dictionary[i]+=1
            else:
                dictionary[i] = 1
        # a: 1 - a: 2 - a: 1 - a: 3 - b: 1
        # b: 1 - b: 2               - a: 3
        # c: 4                      - n: 2
        # d: 2                      - s: 1
        
        biggest_odd = 0
        for i in dictionary.values():
            if i%2==0:
                count_pairs += i
            elif i > biggest_odd:
                biggest_odd = i 
        
        # count_pairs = 2
        # biggest_odd = 3

        return count_pairs+biggest_odd

 
solution = Solution()
input = "aaa"
print(solution.longestPalindrome(input))