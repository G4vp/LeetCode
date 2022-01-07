from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        p1 = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p1] = nums[i]
                p1 += 1
            else:
                j += 1
        l = len(nums) - j
        for i in range(l,len(nums)):
            nums[i] = 0
        
        
        
        