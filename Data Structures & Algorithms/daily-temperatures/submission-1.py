class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack =  []
        
        [30,29,27,36,35,40,28]

        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                continue
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                ans[index] = i - index
            
            stack.append(i)

        return ans





        # ans = []
        
        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             ans.append(j-i)
        #             break
        #         elif j == len(temperatures) - 1:
        #                 ans.append(0)
        # ans.append(0)
        # return ans