class Solution:
    def reverseWords(self, s: str) -> str:
        ns = s.split()
        t = [ns[x] for x in range(len(ns)-1,-1,-1)]
        return ' '.join(t)
        