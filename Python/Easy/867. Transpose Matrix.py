from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        nw_col = [None]*len(matrix)
        nw_Mx = [nw_col[:] for i in range(len(matrix[0]))]
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                nw_Mx[col][row] = matrix[row][col]
        return nw_Mx
                
                