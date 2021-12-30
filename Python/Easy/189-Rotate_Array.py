from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        l = len(nums)-k
        ri = nums[l:]
        le = nums[:l]
        nums[l:] = le
        nums[:l] = ri