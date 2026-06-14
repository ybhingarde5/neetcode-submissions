class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums) / 3

        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        ans = [x for x in hashmap if hashmap.get(x) > length]
        return ans