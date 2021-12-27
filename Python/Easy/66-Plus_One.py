from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        k = [str(x) for x in digits]
        a = int(''.join(k)) + 1
        b = str(a)
        z = [int(x) for x in b]
        return z
        
        