# Leetcode  pro 293:  Flip Game
# https://leetcode.com/problems/flip-game/

class Solution:
    def generatePossibleNextMoves(self, currentState: str ) -> list[str]:
        if len(currentState)==1:
            return []
        result=[]
        for i in range(len(currentState)-1):
            if currentState[i:i+2]=="++":
                result.append(currentState[:i]+"--"+currentState[i+2:])
        return result
      # or
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        s = list(currentState)
        result = []
        for i, c in enumerate(s[:-1]):
            if c == "+" and s[i + 1] == "+":
                s[i] = s[i + 1] = "-"
                result.append("".join(s))
                s[i] = s[i + 1] = "+"
        return result
