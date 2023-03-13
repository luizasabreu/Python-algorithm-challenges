"""
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
"""

class Solution:
    def interpret(self, command: str) -> str:
        result = command.replace("()", "o").replace("(al)", "al")
        return result



solution = Solution()
input = "G()(al)"
print(solution.interpret(input))