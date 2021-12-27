class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        for i in range(len(s)):
            sc = s[i:] + s[0:i]
            
            if sc == goal:
                return True
        return False
