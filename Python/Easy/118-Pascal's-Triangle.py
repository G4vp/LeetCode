from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        p = [[1]]
        
        for i in range(1,numRows):
            lsf = []
            
            for j in range(0,len(p[i-1])-1):
                lsf.append(p[i-1][j]+p[i-1][j+1])
            
            p.append([1]+lsf+[1])
            
        return p