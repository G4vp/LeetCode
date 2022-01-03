from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        
        d = {}
        c = set()
        for a,b in trust:
            d[b] = d.get(b,0)+1
            c.add(a)
        
        for i in d:
            if i not in c and d[i] == n - 1:
                return i
        return -1
    