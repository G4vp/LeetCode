class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        b = num
        s = 0
        while b != 0:
            
            r = b%10
            s = (s*10)+r 
            b //= 10
        
        while s != 0:
            r = s%10
            b = (b*10)+r 
            s //= 10
        
        return b == num