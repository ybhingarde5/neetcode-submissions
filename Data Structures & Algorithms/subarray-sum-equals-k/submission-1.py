class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans = 0
        currSum = 0
        count = {0:1}

        for num in nums:
            currSum += num
            diff = currSum - k
            if diff in count:
                ans += count.get(diff,0)
            count[currSum] = count.get(currSum,0) + 1
        return ans