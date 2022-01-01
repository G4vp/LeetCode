from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
            dt = {}
            
            for ind in range(len(numbers)):
                dt[numbers[ind]] = ind + 1
            
            for ind in range(len(numbers)):
                
                diff = abs(numbers[ind] - target)
                if diff in dt:
                    if ind < dt[diff]:
                        return [ind+1,dt[diff]]
                    else:
                        return [dt[diff],ind+1]

                    
