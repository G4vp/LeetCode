class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = 0
        for i in range(len(columnTitle)):
            d = ord(columnTitle[i])-64
            print(d)
            s += d*(26**(len(columnTitle)-i-1))
        return s