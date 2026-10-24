class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        ans = 0
        hmap = {}
        while j < len(s):
            if s[j] in hmap and hmap[s[j]] >= i:
                i = hmap[s[j]] + 1

            hmap[s[j]] = j
            ans = max(ans, j - i + 1)
            j += 1

        return ans