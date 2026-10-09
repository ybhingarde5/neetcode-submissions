class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        ans = j
        while i <= j:
            k = i + (j - i) // 2
            possible = self.checkSpeed(piles, h, k)
            if possible:
                ans = k
                j = k - 1
            else:
                i = k + 1
            
        return ans

    def checkSpeed(self, piles, h, k):
        ans = 0
        for p in piles:
            ans += (p + k - 1) // k
        
        if ans <= h:
            return k
        else:
            return False
