"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"
Output: true

"""
class Solution:
    def isValid(self, s: str) -> bool:
        pivot = [] 
        for item in s:
            if item == "(" or item == "[" or item == "{":
                pivot.append(item)
            else: 
                if item==")":
                    if len(pivot)>0 and pivot[-1]=="(" :
                        pivot.pop()
                    else:
                        return False
                if item=="]":
                    if len(pivot)>0 and pivot[-1]=="[":
                        pivot.pop()
                    else:
                        return False
                if item=="}":
                    if len(pivot)>0 and pivot[-1]=="{":
                        pivot.pop()
                    else: 
                        return False


        if len(pivot)==0:
            return True
        else: 
            return False


solution = Solution()
input = "()[]{}"
print(solution.isValid(input))