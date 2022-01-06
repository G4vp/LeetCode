from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
    
        r = set()
        c = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    r.add(row)
                    c.add(col)
                
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row in r) or (col in c):
                    matrix[row][col] = 0
            
    