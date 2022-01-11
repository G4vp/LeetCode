from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = {}
        for i in s1.split() + s2.split():
            d[i] = d.get(i,0)+1
        
        va = []
        for i in d:
            if d[i] == 1:
                va.append(i)
        return va