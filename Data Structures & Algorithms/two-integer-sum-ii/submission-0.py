class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        
        i = 0
        j = len(numbers) - 1

        while i < j:
            total = numbers[i] + numbers[j]
            if total > target:
                j-=1
            elif total < target:
                i+=1
            else:
                return [i+1,j+1]




















        # hashmap = {}

        # for i, num in enumerate(numbers):
        #     diff = target - num
        #     if diff in hashmap:
        #         return [diff, num]
        #     hashmap[num] = diff
        # return []
        