class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = 0
        index = 0
        for i in range(len(nums)):
            if nums[i] == 0 and zeroCount == 1:
                return [0] * len(nums)
            elif nums[i] == 0:
                zeroCount += 1
                index = i
            else:
                product *= nums[i]

        ans = [0] * len(nums)
        if zeroCount == 1:
            ans = [0] * len(nums)
            ans[index] = product
            return ans
        
        ans = [product] * len(nums)
        for i in range(len(ans)):
            ans[i] = product // nums[i]
        
        return ans
        


                


        


        # ans = [0] * len(nums)

        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):

        #         if i != j:
        #             product *= nums[j]
                
        #     ans[i] = product 
        
        # return ans





            
            





