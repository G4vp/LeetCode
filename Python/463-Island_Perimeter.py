class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if grid[i][j] == 1:
                    p += self.helper(grid,i,j)
                    grid[i][j] = 2
      
        return p
            
    def helper(self,grid,h,v):
        p = 0
        if self.check(grid,h-1,v): p += 1
        if self.check(grid,h+1,v): p += 1
        if self.check(grid,h,v+1): p += 1
        if self.check(grid,h,v-1): p += 1
        
        return p
    
    def check(self,grid,h,v):
        
        if h < 0 or v < 0 or h >= len(grid) or v >= len(grid[h]):
            return True
        
        return grid[h][v] == 0