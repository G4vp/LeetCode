from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_n = set(nums)
        if len(set_n) < 3: return max(nums)
        
        set_n.remove(max(set_n))
        set_n.remove(max(set_n))
        return max(set_n)