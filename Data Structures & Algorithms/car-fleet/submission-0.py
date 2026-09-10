class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndspeed = []

        for i in range(len(position)):
            posAndspeed.append((position[i], speed[i]))
        
        posAndspeed.sort(reverse=True)

        stack = []
        for pos, speed in posAndspeed:
            time = (target - pos) / speed
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
            
        