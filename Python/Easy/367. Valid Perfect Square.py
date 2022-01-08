class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l = 1
        r = num
        
        while l <= r:
            mid = ((l+r)//2)
            if mid**2 == num:
                return True
            if mid**2 > num:
                r = mid - 1
            else:
                l = mid + 1

        return False
            