from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float: 
        mx = None
        
        p1 = 0
        p2 = 0
        tm = 0

        while p1 < len(nums):
            tm += nums[p1]
            if p1+1 >= k:
                av = tm/k
                if mx == None or av > mx:
                    mx = av
                tm -= nums[p2]
                p2 += 1
            p1 += 1
        
        return mx
            
            