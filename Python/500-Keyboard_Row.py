from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        lst = []
        qw = "qwertyuiop"
        asd = "asdfghjkl"
        zx = "zxcvbnm"
        
        for i in words:
            j = i.lower()
            if len(set(qw).intersection(j)) == len(set(j)):
                lst.append(i)
            
            elif len(set(asd).intersection(j)) == len(set(j)):
                lst.append(i)
            
            elif len(set(zx).intersection(j)) == len(set(j)):
                lst.append(i)
        
        return lst