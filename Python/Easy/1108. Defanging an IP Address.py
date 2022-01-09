class Solution:
    def defangIPaddr(self, address: str) -> str:
        nw_ad = address.replace('.','[.]')
        
        return nw_ad
        