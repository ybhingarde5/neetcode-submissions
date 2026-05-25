class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyre Moore Voting Algorithm

        candidate = 0
        votes = 0

        for num in nums:
            if votes == 0:
                candidate = num
                votes += 1
            elif candidate == num:
                votes += 1
            else:
                votes -= 1
        
        return candidate











        # nums.sort()
        # count, num = 0, 0
        # i = 0
        # while i < len(nums):
        #     j = i
            
        #     while j < len(nums) and nums[i] == nums[j]:
        #         j+=1

        #     freq = j - i

        #     if freq > count:
        #         count = freq
        #         num = nums[i]
            
        #     i = j
            
        # return num


        