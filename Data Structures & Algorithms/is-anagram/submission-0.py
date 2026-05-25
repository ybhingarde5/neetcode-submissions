class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s) != len(t):
            return False
        

        sHash = {}
        tHash = {}

        for c in s:
            if c in sHash:
                sHash[c] += 1
            else:
                sHash[c] = 1
        for c in t:
            if c in tHash:
                tHash[c] += 1
            else:
                tHash[c] = 1
        
        if sHash == tHash:
            return True
        return False