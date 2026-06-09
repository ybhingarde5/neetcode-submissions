class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        ans = 0

        for num in nums:
            if (num - 1) not in numSet:
                length = 1
                temp = num
                while (temp + 1) in numSet:
                    length += 1
                    temp += 1
                ans = max(ans, length)
        
        return ans
                



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # hashmap = {}
        # ans = 0
        # l,h= 0,0
        # def findSeq(num: int, ans: int):
        #     ltemp = num
        #     htemp = num

        #     temp1 = num
        #     while temp1 - 1 in hashmap:
        #         ltemp = temp1 - 1
        #         temp1 -= 1 

        #     temp2 = num
        #     while temp2 + 1 in hashmap:
        #         htemp = temp2 + 1
        #         temp2 += 1
            
        #     val =  (htemp-ltemp)+1
        #     if val > ans:
        #         return (val, ltemp, htemp)
        #     else: ans
            
        # for num in nums:
        #     if not l <= num <= h:
        #         (val, ltemp, htemp) = findSeq(num, ans)
        #         if ltemp and htemp:
        #             l = ltemp, h = htemp
                    
        #     hashmap[num] = hashmap.get(num, 0) + 1

        # return ans