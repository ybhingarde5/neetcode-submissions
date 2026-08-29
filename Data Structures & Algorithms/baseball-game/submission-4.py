class Solution:
    def calPoints(self, operations: List[str]) -> int:

        ans = []

        for op in operations:
            
            if op == "+":
                ans.append(ans[-1] + ans[-2])
            elif op == "D":
                ans.append(2 * ans[-1])
            elif op == "C":
                ans.pop()
            else:
                ans.append(int(op))

        return sum(ans)

































        # stack = []
        # for ops in operations:
        #     if ops == "+":
        #         stack.append(stack[-1] + stack[-2])
        #     elif ops == 'C':
        #         stack.pop()
        #     elif ops == 'D':
        #         stack.append(stack[-1] * 2)
        #     else:
        #         stack.append(int(ops))
        # ans = 0
        # for num in stack:
        #     ans += num
        # return ans
