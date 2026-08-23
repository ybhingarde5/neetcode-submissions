class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() #-> nlogn
        ans = set()
        i = 0

        while i < len(nums) - 2:
            j = i+1
            k = len(nums) - 1

            while j < k:
                total = nums[j] + nums[k] + nums[i]
                if total > 0:
                    k-=1
                elif total < 0:
                    j+=1
                else:
                    ans.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
            i+=1

        return [list(t) for t in ans]



























        # nums.sort()
        # n = len(nums)
        # ans = []

        # for i in range(n-2):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     j = i+1
        #     k = n-1
        #     while j < k:
        #         s = nums[i] + nums[j] + nums[k]
        #         if s == 0:
        #             ans.append([nums[i] , nums[j] , nums[k]])
        #             j+=1
        #             k-=1
        #             while j < k and nums[j] == nums[j-1]:
        #                 j+=1
        #             while j< k and nums[k] == nums[k+1]:
        #                 k-=1
        #         else:
        #             if s > 0:
        #                 k-=1
        #             else:
        #                 j+=1
                    
        # return ans
                


        

        # n = len(nums)
        # ans = []
        # nums.sort()
        # for i in range(n-2):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     j = i+1
        #     k = n-1
        #     while j < k:
        #         s = nums[i] + nums[j] + nums[k]
        #         if s == 0:
        #             ans.append([nums[i], nums[j] , nums[k]])
        #             j+=1
        #             k-=1
        #             while j<k and  nums[j] == nums[j-1]:
        #                 j+=1
        #             while j<k and nums[k] == nums[k+1]:
        #                 k-=1
        #         elif s > 0:
        #             k-=1
        #         else:
        #             j+=1
        # return ans
                    