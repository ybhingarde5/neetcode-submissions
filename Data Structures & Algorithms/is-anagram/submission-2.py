class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True


        # if len(s) != len(t):
        #     return False
        
        # sHash = {}
        # tHash = {}

        # for c in s:
        #     if c in sHash:
        #         sHash[c] += 1
        #     else:
        #         sHash[c] = 1
        # for c in t:
        #     if c in tHash:
        #         tHash[c] += 1
        #     else:
        #         tHash[c] = 1
        
        # if sHash == tHash:
        #     return True
        # return False