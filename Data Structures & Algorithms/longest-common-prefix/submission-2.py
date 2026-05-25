class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]

        for s in strs:
            if len(s) == 0:
                return ""
            i = 0
            while i < len(s) and i < len(word):

                if s[i] != word[i]:
                    break
                
                i+=1
            word = word[:i]
        
        return word
                