from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sumIndex = list()
        for index1 in range(len(nums)):
            for index2 in range(index1+1,len(nums)):
                if nums[index1] + nums[index2] == target:
                    sumIndex += [index1,index2]
        return sumIndex