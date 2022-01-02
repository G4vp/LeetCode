from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mx = None
        sm = None
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        for i in d:
            if sm == None or sm < d[i]:
                mx = i
                sm = d[i]
        return mx