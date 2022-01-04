class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]
        
        k = ''.join(['1' if x == '0' else '0' for x in b])
        
        return int(k,2)
    