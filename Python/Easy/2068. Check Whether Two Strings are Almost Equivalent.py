class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        D_1 = {}
        D_2 = {}
        
        for ch in word1:
            D_1[ch] = D_1.get(ch,0)+1
        for ch in word2:
            D_2[ch] = D_2.get(ch,0)+1
            
        for key in set(D_1.keys())|set(D_2.keys()):
            if abs(D_1.get(key,0) - D_2.get(key,0)) > 3:
                return False

        return True