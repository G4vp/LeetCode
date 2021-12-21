class Solution:
    def isPowerOfThree(self, n: int, s = 0) -> bool:
        if 3**s > n:
            return False
        elif 3**s == n:
            return True
        else:
            return self.isPowerOfThree(n,s+1)