class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        k = path.split("/")
        print(k)
        for s in k:
            if s in ["", "."]:
                continue
            
            if s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        
        print(stack)
        
        return "/" + "/".join(stack)