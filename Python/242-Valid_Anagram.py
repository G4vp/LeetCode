class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ts = set(s).union(t)
        
        for i in ts:
            if s.count(i) != t.count(i):
                return False
        return True