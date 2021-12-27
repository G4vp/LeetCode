class Solution:
    def isValid(self, s: str) -> bool:
        
        s2 = s[:]
        
        
        while s2.find('()') != -1 or s2.find('[]') != -1 or s2.find('{}') != -1:
            
            s2 = s2.replace('()','')
            s2 = s2.replace('[]','')
            s2 = s2.replace('{}','')
        
        return len(s2) == 0
        
                
                