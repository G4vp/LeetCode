class Solution:
    # Python solution without find() or index()
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle in haystack:
            return  -1
        if len(needle) < 1:
            return 0
        
        for ind,val in enumerate(haystack):
            if val == needle[0]:
                if haystack[ind:ind+len(needle)] == needle:
                    return ind
        
            
        
