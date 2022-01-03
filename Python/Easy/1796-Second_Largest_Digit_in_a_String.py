class Solution:
    def secondHighest(self, s: str) -> int:
        l = list(set([int(x) for x in s if x.isdigit()]))
        
        if len(l) > 1:
            l.remove(max(l))
            return max(l)
        else:
            return -1
        