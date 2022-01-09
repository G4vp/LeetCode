from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        for ind, ele in enumerate(nums):
            if ele not in nums[:ind] + nums[ind+1:]:
                return ele
        
            