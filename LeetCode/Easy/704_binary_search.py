"""
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while(start<=end):
            middle = int((start+end)/2)
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                end = middle-1
            elif nums[middle]< target:
                start = middle+1
        return -1
              


solution = Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(solution.search(nums, target))