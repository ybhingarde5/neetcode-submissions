class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count, num = 0, 0
        i = 0

        while i < len(nums):
            j = i
            
            while j < len(nums) and nums[i] == nums[j]:
                j+=1

            freq = j - i

            if freq > count:
                count = freq
                num = nums[i]
            
            i = j
            
        return num


        