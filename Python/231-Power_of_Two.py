class Solution:
    def isPowerOfTwo(self, n: int, s = 0) -> bool:
        if 2**s > n:
            return False
        elif 2**s == n:
            return True
        else:
            return self.isPowerOfTwo(n,s+1)