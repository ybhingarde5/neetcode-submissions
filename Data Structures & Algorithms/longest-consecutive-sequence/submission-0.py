class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        ans = 0

        def findSeq(num: int, ans: int):
            ltemp = num
            htemp = num
            temp1 = num
            while temp1 - 1 in hashmap:
                ltemp = temp1 - 1
                temp1 -= 1 
            temp2 = num
            while temp2 + 1 in hashmap:
                htemp = temp2 + 1
                temp2 += 1
            
            return  max((htemp-ltemp)+1, ans) 
            


        for num in nums:
            ans = findSeq(num, ans)
            hashmap[num] = hashmap.get(num, 0) + 1

        return ans
