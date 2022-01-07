from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        sl = len(s1) 
        SZ = Counter(s1)
        for i in range(sl,len(s2)+1):
            a = abs(sl-i)
            bs = s2[a:i]
            if  Counter(bs) == SZ:
                return True
        return False
    
    