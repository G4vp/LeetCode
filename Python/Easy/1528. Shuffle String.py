from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_cop = ['']*len(indices)
        for i in range(len(s)):
            s_cop[indices[i]] = s[i]
        return ''.join(s_cop)
            
        