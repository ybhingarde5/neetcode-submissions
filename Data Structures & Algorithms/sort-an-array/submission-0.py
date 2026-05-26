class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0

        while i < n:
            j = i

            while j < n:
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                j+=1
            
            i+=1
        
        return nums