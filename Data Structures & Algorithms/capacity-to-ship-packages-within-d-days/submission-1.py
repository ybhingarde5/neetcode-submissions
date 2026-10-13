class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i = max(weights)
        j = sum(weights)
        ans = 0
        while i <= j:

            capacity = i + (j-i) // 2

            res = self.check(capacity, weights, days)
            
            if res:
                ans = capacity
                j = capacity - 1
            else:
                i = capacity + 1
        return ans



    def check(self, capacity, weights, days):
        usedDays = 1
        loadedWeights = 0

        for w in weights:
            if loadedWeights + w > capacity:
                loadedWeights = w
                usedDays += 1
            else:
                loadedWeights = loadedWeights + w
        
        return usedDays <= days

                


