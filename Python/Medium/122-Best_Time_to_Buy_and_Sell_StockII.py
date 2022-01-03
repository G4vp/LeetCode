from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        mn = None
        for p1 in range(len(prices)):            
            if mn == None or prices[p1] < mn:
                mn = prices[p1]
            else:
                print(prices[p1],pro,mn)
                pro += prices[p1] - mn
                mn = prices[p1]
        return pro
        