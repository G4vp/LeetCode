class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        t1 = self.skere(t)
        s1 = self.skere(s)
        return s1 == t1
        
        
        
        
    def skere(self,s):
        dit = {}
        ls = []
        counter = 0
        for i in s:
            if i in dit.keys():
                ls.append(dit.get(i))
            else:
                counter += 1
                dit[i] = counter
                ls.append(counter)
        return ls