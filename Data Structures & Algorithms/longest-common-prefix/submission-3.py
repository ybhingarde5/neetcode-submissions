class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]

        for s in strs:

            i = 0 

            while i < min(len(word), len(s)):
                if word[i] != s[i]:
                    break
                i+=1
            
            word = s[:i]
        
        return word