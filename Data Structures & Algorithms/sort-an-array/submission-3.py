class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i] , nums[j] = nums[j], nums[i]
        
        return nums

        



        # bubble sort
        # end = len(nums)
        # i , j = 0, 1
        # while end > 0:
        #     while j < end:
        #         if nums[j] < nums[i]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #         i+=1
        #         j+=1
        #     i = 0
        #     j = 1
        #     end-=1
        # return nums



        # two pointer sort [selection srot]
        # n = len(nums)
        # i = 0

        # while i < n:
        #     j = i

        #     while j < n:
        #         if nums[j] < nums[i]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #         j+=1
            
        #     i+=1
        
        # return nums