from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hs2 = {}
        for i in nums2:
            hs2[i] = hs2.get(i,0) + 1
        
        ar = []
        for i in nums1:
            if i in hs2 and hs2[i] != 0:
                ar.append(i)
                hs2[i] -= 1
        return ar
        
