from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        d = {}
        for w in ''.join(words):
            d[w] = d.get(w,0)+1
                
        for i in d:
            if d[i]%len(words) != 0:
                return False
        return True