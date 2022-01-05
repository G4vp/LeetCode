class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        d = {}
        for i in magazine:
            d[i] = d.get(i,0)+1
            
        for i in ransomNote:
            
            if i in d and d[i] > 0:
                d[i] -= 1
            else:
                return False
        return True