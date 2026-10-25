class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq = {}
        for c in s1:
            s1freq[c] = s1freq.get(c, 0) + 1
        def checkSubstring(i, j):
            s2freq = {}
            for c in s2[i:j]:
                s2freq[c] = s2freq.get(c, 0) + 1
            if s1freq == s2freq:
                return True
            else:
                return False


            
        for i in range(len(s2)):
            if s2[i] in s1:
                check = checkSubstring(i, i+len(s1))
                if check:
                    return True
        
        return False




