class Solution:
    def intToRoman(self, num: int) -> str:
        n = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        r = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        
        an = ''        
        for i in range(13):
            t = num//n[i] 
            num -= t*n[i]
            an += t*r[i]
        return an