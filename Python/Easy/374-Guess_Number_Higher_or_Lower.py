# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
def guess(n):
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        h = n
        while(l <= h):
            mid = (h + l)//2
            if(guess(mid) == 0):
                return mid
            elif(guess(mid) == 1):
                l = mid + 1
            else:
                h = mid - 1