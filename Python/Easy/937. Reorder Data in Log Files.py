from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        dig = []
        let = []
        
        for i in logs:
            if i.split()[1].isdigit():
                dig.append(i)
            else:
                identifier, content = i.split(' ',1)
                let.append((content,identifier))
        sorted_let = sorted(let)
        
        new_sort_let = [identifier + ' ' + content for content,identifier in sorted_let]
        
        return new_sort_let+dig