from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = {   "a":".-",
                "b":"-...",
                "c":"-.-.",
                "d":"-..",
                "e":".",
                "f":"..-.",
                "g":"--.",
                "h":"....",
                "i":"..",
                "j":".---",
                "k":"-.-",
                "l":".-..",
                "m":"--",
                "n":"-.",
                "o":"---",
                "p":".--.",
                "q":"--.-",
                "r":".-.",
                "s":"...",
                "t":"-",
                "u":"..-",
                "v":"...-",
                "w":".--",
                "x":"-..-",
                "y":"-.--",
                "z":"--.."}
        
        l = []
        for i in words:
            ts = ''
            for j in i:
        
                    ts += m[j]
                    
            if not ts in l:
                l.append(ts)
        
        return len(l)