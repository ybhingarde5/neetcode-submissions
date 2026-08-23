class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            height = min(heights[i], heights[j])
            width = j - i

            ans = max(ans, height * width)

            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return ans

            
