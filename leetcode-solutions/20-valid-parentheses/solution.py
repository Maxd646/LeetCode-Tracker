# Leetcode 20: Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        pairs= {')':'(','}':'{',']': '['}
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack[-1]!= pairs[char]:
                    return False
                stack.pop()
        return len(stack)==0
