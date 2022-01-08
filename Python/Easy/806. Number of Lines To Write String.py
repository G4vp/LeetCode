from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        line = 1
        pixel = 0
        
        for i in s:
            wid_pix = widths[ord(i)-97]
            if wid_pix + pixel > 100:
                line += 1
                pixel = 0
            pixel += wid_pix
        return [line,pixel]
        