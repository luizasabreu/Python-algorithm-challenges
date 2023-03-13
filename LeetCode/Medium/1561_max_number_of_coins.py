"""
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:
In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.
Return the maximum number of coins that you can have.
 

Example 1:
Input: piles = [2,4,1,**2**,**7**,8]
Output: 9
Explanation: Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with 7 coins and Bob the last one.
Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with 2 coins and Bob the last one.
The maximum number of coins which you can have are: 7 + 2 = 9.

"""

from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles, reverse=True) # [2,4,1,2,7,8]
        result = 0
        times = int(len(sorted_piles)/3)
        start = 0
        end = 2
        for i in range(times): #[8,7,4] [2,2,1]
            new_pile = sorted_piles[start:end+1]
            result+=new_pile[1]
            start+=3
            end+=3
        return result
            



 
solution = Solution()
input = [2,4,1,2,7,8]
print(solution.maxCoins(input))