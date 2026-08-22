class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                del nums[i+1]
            else:
                i+=1

        return len(nums)
        # map = {}
        # ans = []

        # for num in nums:
        #     if num not in map:
        #         ans.append(num)

        #     map[num] = map.get(num,0) + 1

        # nums[:len(ans)] = ans
        # return len(ans)