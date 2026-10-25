class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        ans = 0
        maxfreq = 0
        hmap = {}

        while j < len(s):
            windowLen = j-i+1
            hmap[s[j]] = hmap.get(s[j], 0) + 1
            maxfreq = max(maxfreq, hmap[s[j]])

            if (windowLen - maxfreq) > k:
                hmap[s[i]] -=1
                i+=1
            
            else:
                ans=max(ans, windowLen)
            j+=1
        
        return ans
        
        