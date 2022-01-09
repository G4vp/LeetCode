from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def convert(s):
            ls = {}
            n_s = ''
            for i,v in enumerate(s):
                if v not in ls:
                    ls[v] = str(i)
                n_s += ls[v]
            return n_s
        
        p = convert(pattern)
        lst = []
        for i in words:
            w = convert(i)
            if  w == p:
                lst.append(i)
        return lst
        
        
                