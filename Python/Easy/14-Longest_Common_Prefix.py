from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        data = ''
        total = 0
        counter = 0
        shit = []

        for index,val in enumerate(strs):

            for i in range(len(val)):

                for j in range(0,len(strs)):

                    if strs[j].startswith(val[0:i+1]):
                        counter += 1
                    if counter >= total:
                        total = counter
                        data = val[0:i+1]
                shit.append(counter)
                counter = 0
        if total == 1 and len(strs) > 1 or total < len(strs):
            return ''
        return data

