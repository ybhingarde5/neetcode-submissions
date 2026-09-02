class StockSpanner:

    def __init__(self):
        self.stack = [None]
        self.ansArr = []
        
    def next(self, price: int) -> int:
        tempStack = self.stack[:]
        ans = 1
        while tempStack and tempStack[-1] != None and tempStack[-1] <= price:
            tempStack.pop()
            ans += 1
        
        self.stack.append(price)
        self.ansArr.append(ans)

        return ans


