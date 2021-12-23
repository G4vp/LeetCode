from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        
        for i in range(len(nums)):
            s = nums[i]
            if nums[i] != 0:
                nums[i] = nums[l]
                nums[l] = s
                
                l += 1
        return l