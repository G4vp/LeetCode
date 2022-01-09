from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mx = 0
        for i in sentences:
            mx = max(mx,len(i.split()))
        return mx
    
