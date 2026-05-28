class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i,j,k = 0,0,len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                nums[i] , nums[j] = nums[j], nums[i]
                i+=1
                j+=1
            elif nums[j] == 2:
                nums[k] , nums[j] = nums[j], nums[k]
                k-=1
            else:
                j+=1
        return nums


        # i = 0

        # while i < len(nums):
        #     j = i

        #     while j < len(nums):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #         j+=1
            
        #     i += 1
        
        # return nums
