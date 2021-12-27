class Solution:
    def romanToInt(self, s: str) -> int:
        romans_numbers = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        number = 0

        for i in range(len(s)):
            if romans_numbers.get(s[i-1]) < romans_numbers.get(s[i]) and i != 0:
                number -= romans_numbers.get(s[i-1])*2
            number += romans_numbers.get(s[i])
        return number