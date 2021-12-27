from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        l = ''
        for i in words:
            l += i
            if l == s:
                return True
                
        return False
        
        