class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dic = {}
        for i in s:
            s_dic[i] = s_dic.get(i,0)+1
        
        for i in range(len(s)):
            if s_dic[s[i]] == 1:
                return i
        return -1
        