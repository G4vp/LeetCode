class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        out = tp = ''
        
        for i in s:
            fd = tp.find(i)
            if fd > -1:
                tp = tp[fd+1:]
                
            tp += i
            
            if len(tp) > len(out):
                out = tp
        return len(out)