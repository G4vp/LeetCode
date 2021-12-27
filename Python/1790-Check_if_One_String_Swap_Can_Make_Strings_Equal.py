class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if s1 == s2:
            return True
        
        if set(s1) != set(s2):
            return False
        
        c = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c += 1
                
        return c == 2



