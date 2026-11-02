class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        total = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                total = sum(nums[i:j+1])
                if total >= target:
                    ans = min(len(nums[i:j+1]), ans)
                    break
        
        if ans == float('inf'):
            return 0
        return ans