class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) < 1: return True
        
        p1 = 0
        
        for i in t:
            if i == s[p1]:
                p1 += 1
            if p1 == len(s):
                return True
        return False