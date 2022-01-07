class Solution:
    def reverseWords(self, s: str) -> str:
        
        n = s.split()
        for i in range(len(n)):
            n[i] = n[i][::-1]
        return ' '.join(n)