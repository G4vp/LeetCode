from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        a, b, c = set(nums1),set(nums2),set(nums3)
        
        return (a&b)|(a&c)|(b&c)