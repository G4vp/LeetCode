class Solution:
    def tribonacci(self, n: int) -> int:
        f = [0,1,1]
        for i in range(2,n):
            f.append(f[i]+f[i-1]+f[i-2])
        return f[n]