class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height) 

        leftMax = [height[0]] + [0] * (n - 1)
        rightMax =  [0] *( n -1) + [height[-1]]

        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1], height[i])

        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        
        for i in range(n):
            ans += min(leftMax[i], rightMax[i]) - height[i]
        
        return ans


        # i = 0
        # j = 1
        # ans = 0

        # while i < n:

        #     if height[i] <= height[j]:
        #         width = j - i - 1
        #         currHeight = min(height[i], height[j])
        #         totalArea = width * currHeight
        #         actualArea = totalArea - sum(height[i+1:j])
        #         ans += actualArea
        #         i = j
        #         j += 1
        #     else:
        #         j+=1
        # return ans


        # n = n
        # i = 0
        # j = n - 1
        # maxI = height[i]
        # maxJ = height[j]
        # ans = 0
        # while i < j:
        #     if height[i] < height[j]:
        #         i+=1
        #         maxI = max(maxI, height[i])
        #         ans += maxI - height[i] 
        #     else:
        #         j-=1
        #         maxJ = max(maxJ, height[j])
        #         ans += maxJ - height[j]
        # return ans

        
        # n = n
        # i = 0
        # j = 1
        # ans = 0
        # while i < n-1:
        #     if height[i] == height[j]:
        #         while height[i] == height[j]:
        #             j+=1
        #         i = j-1
        #     elif height[i] > height[j]:
        #         blockCount = 0
        #         while height[i] > height[j]:
        #             blockCount += height[j]
        #             j+=1
        #         h = min(height[i], height[j])
        #         breadth = (j - i) - 1
        #         areaFilledWithWater = (h * breadth) - blockCount
        #         ans +=  areaFilledWithWater
        #         i = j
        #         j += 1
        #     else:
        #         i+=1 
        #         j+=1
        # return ans
