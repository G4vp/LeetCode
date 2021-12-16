class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join([x.lower() for x in s if x.isalnum()])
        return s2 == s2[::-1]