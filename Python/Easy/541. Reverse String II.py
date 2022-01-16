class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        b = True
        prev = 0
        for i in range(k,len(s)+k,k):
            if b:
                res += s[prev:i][::-1]
            else:
                res += s[prev:i]
            b = not b
            prev = i
        return res
            
            
