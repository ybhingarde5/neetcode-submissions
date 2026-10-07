class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = []
        while i < j:
            ans.append(nums[i])
            ans.append(nums[j])
            i+=1
            j-=1
        nums[:] = ans