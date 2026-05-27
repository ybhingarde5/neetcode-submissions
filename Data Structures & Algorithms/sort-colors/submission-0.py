class Solution:
    def sortColors(self, nums: List[int]) -> None:
        

        i = 0

        while i < len(nums):
            j = i

            while j < len(nums):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                j+=1
            
            i += 1
        
        return nums
