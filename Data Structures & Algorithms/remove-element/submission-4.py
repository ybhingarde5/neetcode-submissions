class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0

        for j in range(len(nums)):
            
            if nums[j] != val:
                nums[i] , nums[j] = nums[j], nums[i]
                i+=1
        
        return i






        # num = []

        # for n in nums:
        #     if n != val:
        #         num.append(n)
        
        # for i in range(len(num)):
        #     nums[i] = num[i]
        # return len(num)

        