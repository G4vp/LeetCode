class Solution:
    def fib(self, n: int) -> int:
        
        ls = [0,1]
        for i in range(1,n):
            ls.append(ls[i]+ls[i-1])
        return ls[n]