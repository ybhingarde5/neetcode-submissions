class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0 
        j = 0
        ans = len(nums) + 1
        psum = 0
        while i < len(nums) and j < len(nums):
            psum += nums[j]
            while psum >= target:
                ans = min(len(nums[i:j+1]), ans)
                psum -= nums[i]
                i+=1
            j+=1
        
        if ans == len(nums) + 1:
            return 0
        return ans






        # ans = float('inf')
        # total = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         total = sum(nums[i:j+1])
        #         if total >= target:
        #             ans = min(len(nums[i:j+1]), ans)
        #             break
        
        # if ans == float('inf'):
        #     return 0
        # return ans