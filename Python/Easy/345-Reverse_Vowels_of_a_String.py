class Solution:
    def reverseVowels(self, s: str) -> str:
        f = list(s)
        l = 0
        r = len(s)-1
        al = 'aeiouAEIOU'
        
        while l < r:
            
            if f[l] in al and f[r] in al:
                f[l], f[r] = f[r], f[l]
                l += 1
                r -= 1
                
            if f[l] not in al:
                l += 1
                
            if f[r] not in al:
                r -= 1
        return ''.join(f)