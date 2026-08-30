class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))
                continue

            lastElem = stack.pop()
            secondlastElem = stack.pop()

            if t == "+":
                stack.append(secondlastElem + lastElem)
            elif t == "-":
                stack.append(secondlastElem - lastElem)
            elif t == "*":
                stack.append(secondlastElem * lastElem)
            elif t == "/":
                stack.append(int(secondlastElem / lastElem))

        return stack[-1]