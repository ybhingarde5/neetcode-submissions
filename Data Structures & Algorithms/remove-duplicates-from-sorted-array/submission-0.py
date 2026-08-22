class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        map = {}
        ans = []

        for num in nums:
            if num not in map:
                ans.append(num)

            map[num] = map.get(num,0) + 1
        nums[:len(ans)] = ans
        return len(ans)