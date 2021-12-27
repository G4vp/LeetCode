from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        #Find the minimun absolute difference
        def minimunN(sA):
            n = None
            for i in range(len(sA)-1):
                ab = abs(sA[i] - sA[i+1])
                if n == None or  ab < n:

                    n = ab
            return n

        #Pair the elements with the minimun absolute difference
        newLst = sorted(arr)
        n = minimunN(newLst)
        Lst = list()
        for i in range(len(newLst)-1):
            if abs(newLst[i] - newLst[i+1]) <= n:
                Lst.append([newLst[i],newLst[i+1]])
        return Lst
    
