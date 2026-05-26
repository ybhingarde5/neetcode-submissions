class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        end = len(nums)
        i , j = 0, 1


        while end > 0:

            while j < end:
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j+=1

            i = 0
            j = 1
            end-=1
        return nums







        # two pointer sort
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