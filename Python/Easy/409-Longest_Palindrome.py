class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        d = {}
        g = 0
        for i in s:
            d[i] = d.get(i,0)+1
        
        k = True
        for i in d:
            
            if d[i]%2 == 0:
                g += d[i]
            elif k:
                g += d[i]
                k = False
            else:
                g += d[i]-1
        return g
                