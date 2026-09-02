class StockSpanner:

    def __init__(self):
        self.stack = []
        # self.ansArr = []

        # [[], [100], [80], [60], [70], [60], [75], [85]]

    def next(self, price: int) -> int:
        # tempStack = self.stack[:]
        ans = 1
        # while tempStack and tempStack[-1] != None and tempStack[-1] <= price:
        #     tempStack.pop()
        #     ans += 1

        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack[-1][1]
            self.stack.pop()
        
        self.stack.append((price,ans))
        # self.ansArr.append(ans)

        return ans


