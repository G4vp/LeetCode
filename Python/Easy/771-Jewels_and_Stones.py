class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = dict()
        for i in stones:
            d[i] = d.get(i,0) + 1
            
        c = 0
        for i in jewels:
            c += d.get(i,0)
            
        return c