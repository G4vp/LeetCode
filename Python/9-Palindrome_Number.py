class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0): return False

        number_copy = x
        reverse_number = 0
        while(number_copy > 0):
            reverse_number = (reverse_number*10)+number_copy%10
            number_copy //= 10
        
        return x == reverse_number
    
