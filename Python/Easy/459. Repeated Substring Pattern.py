import collections
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        
        t = s[0]
        for i in range(1,len(s)):
            ls = len(s)//len(t)
            if t * ls == s:
                return True
            t += s[i]
        return False
