class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        mx = 0
        ls = 0
        prev = None
        for i in nums:
            if prev != None:
                if prev >= i:
                    ls = 0
            ls += 1      

            if ls > mx:
                mx = ls
            prev = i     
        
        return mx
    