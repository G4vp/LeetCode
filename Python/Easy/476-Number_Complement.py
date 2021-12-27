class Solution:
    def findComplement(self, num: int) -> int:
        b = str(bin(num)).replace('0b','')
        b = b.replace('0','2')
        b = b.replace('1','0')
        b = b.replace('2','1')
        
        return int(b,2)