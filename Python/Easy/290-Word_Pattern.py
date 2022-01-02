class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        st = s.split()
        if len(pattern) != len(st) : return False

        for i,j in zip(pattern,st):
            if not i in d.keys():
                if not j in d.values():
                    d[i] = j
                else:
                    return False
            else:
                if d[i] != j:
                    return False
        return True
            