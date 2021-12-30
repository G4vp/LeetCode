from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if len(nums) < 1 : return nums
        
        ls = []
        prev = None
        ts = []
        for i in nums:
            if prev != None and prev + 1 != i:        
                ls.append(self.helper(ts))
                ts = []
                    
            ts.append(str(i))
            prev = i
        ls.append(self.helper(ts))
        return ls
    
    
    def helper(self,ts):
        if len(ts) > 1:
            return ts[0] + "->" + ts[-1]
        else:
            return ts[0]