from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        Ans = 0
        k_val = tickets[k]
        for i in range(len(tickets)):
            
            if i <= k:
                Ans += min(k_val,tickets[i])
            else:   
                Ans += min(k_val-1,tickets[i])
        return Ans