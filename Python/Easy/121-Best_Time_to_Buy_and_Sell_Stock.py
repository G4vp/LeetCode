from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        pro = 0
        
        mn = None
        
        
        for p1 in range(len(prices)):            
            if mn == None or prices[p1] < mn:
                mn = prices[p1]
            
            if prices[p1] - mn > pro:
                pro = prices[p1] - mn
        
        return pro
        