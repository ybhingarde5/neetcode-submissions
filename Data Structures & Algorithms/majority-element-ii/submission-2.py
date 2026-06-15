class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        num1, num2 = 0,0
        cnt1, cnt2 = 0,0

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = num
                cnt1 = 1
            elif cnt2 == 0:
                num2 = num
                cnt2 = 1
            else:
                cnt1-=1
                cnt2-=1

        cnt1, cnt2 = 0, 0 
        for num in nums:
            if num == num1:
                cnt1+=1
            elif num == num2:
                cnt2+=1
        

        ans = []
        if cnt1 > len(nums) // 3:
            ans.append(num1)
        if cnt2 > len(nums) // 3:
            ans.append(num2)
        

        return ans





        # length = len(nums) / 3

        # hashmap = {}

        # for num in nums:
        #     hashmap[num] = hashmap.get(num, 0) + 1

        # ans = [x for x in hashmap if hashmap.get(x) > length]
        # return ans