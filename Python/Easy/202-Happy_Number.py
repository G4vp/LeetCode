class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        lst = []
        while n != 1:
            c = 0
            hp = n
            while hp > 0:
                c += (hp%10)**2
                hp //= 10
            n = c
            
            if n in lst:
                return False
            
            lst.append(n)

        return True
            
        
        