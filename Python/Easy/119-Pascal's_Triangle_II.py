from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        p = [[1]]
        
        p1 = 1
        while len(p) != rowIndex + 1:
            ls = []
            for i in range(1,len(p[p1-1])):
                ls.append(p[p1-1][i-1]+p[p1-1][i])
            
            
            p.append([1]+ls+[1])
            p1 += 1
            
        return p[-1]