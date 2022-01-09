class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
    
        def converter(num):
            le = len(num)-1
            n = 0
            for i in num:
                n += (ord(i)-48)*10**le
                le -= 1
            return n
        
        return str(converter(num1) + converter(num2))
            