from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        nw_lst = []
        for i in image:
            sl = [0 if x == 1 else 1 for x in i[::-1]]
            nw_lst.append(sl)
        return nw_lst