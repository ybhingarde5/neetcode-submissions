class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
                continue
            
            tempArr = []
            while stack[-1] != "[":
                tempArr.append(stack.pop())
            merged_string = "".join(tempArr[::-1])
            stack.pop()

            digit = ""
            while stack and stack[-1].isdigit():
                digit+=stack.pop()

            digit = int(digit[::-1])
            temp = merged_string
            print(temp, digit)
            stack.append(temp*digit)
            print(stack)
        
        return "".join(stack)
