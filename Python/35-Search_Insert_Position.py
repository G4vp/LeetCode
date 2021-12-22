from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for ind,val in enumerate(nums):
            if val >= target:
                return ind
        return len(nums)