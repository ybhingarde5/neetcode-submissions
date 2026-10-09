class Solution:
    def mySqrt(self, x: int) -> int:
        
        for i in range(0,x+1):
            square = i * i
            if square == x:
                return i
            elif square > x:
                return i - 1
        
        return 0
