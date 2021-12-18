from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        
        s = list(s)
        x = []
        
        for i in range(len(s)):
            if s[i] == c:
                s[i] = 0
                x.append(i)
                
        for i in range(len(s)):
            s[i] = min([abs(j-i) for j in x])
            print(s)
        return s            
            