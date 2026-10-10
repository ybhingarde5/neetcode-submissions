class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i = max(weights)
        j = sum(weights)
        ans = float('inf')
        while i <= j:
            weight = i + (j - i) // 2

            canShip = self.check(weight, weights, days)
            if canShip:
                ans = min(weight, ans)
                j = weight - 1
            else:
                i = weight + 1
        return ans

    def check(self, capacity:int, weights:List[int], days:int):
        loadedWeight = 0
        usedDays = 1
        
        for w in weights:
            if loadedWeight + w > capacity:
                usedDays += 1
                loadedWeight = w
            else:
                loadedWeight += w
        
        return usedDays <= days 
                


