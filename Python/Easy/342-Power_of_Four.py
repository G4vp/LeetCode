class Solution:
    def isPowerOfFour(self, n: int,s=0) -> bool:
        if 4**s > n:
            return False
        elif 4**s == n:
            return True
        else:
            return self.isPowerOfFour(n,s+1)