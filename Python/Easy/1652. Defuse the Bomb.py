class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        
        nws = code[:]
        cd = code*2 
        for i in range(len(nws)):
            if k > 0:
                nws[i] = sum(cd[i+1:i+1+k])
            else:
                nws[i] = sum(cd[i+len(code)+k:i+len(code)])
        return nws
