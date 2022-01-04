from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        l = set(list1).intersection(list2)
        d = {}
        
        lst = []
        mn = None
        for i in l:
            s = list1.index(i) + list2.index(i)
            if mn == None or s == mn:
                lst.append(i)
                mn = s
            elif mn > s:
                lst = []
                lst.append(i)
                mn = s
        return lst
            
        
        