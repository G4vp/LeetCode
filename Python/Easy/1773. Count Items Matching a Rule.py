from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {"type":0,"color":1,"name":2}
        c = 0
        
        l = 0
        r = len(items)-1
        
        while l <= r:
            if l != r and items[l][d[ruleKey]] == ruleValue:
                c += 1
            if items[r][d[ruleKey]] == ruleValue:
                c += 1
            l += 1
            r -= 1

        return c