class Solution:
    def mySqrt(self, x: int) -> int:
        
        i = 0
        j = x

        while i <= j:
            num = i + (j - i) // 2
            print(num, f"({i,j})")
            square = num * num
            if square == x:
                return num
            if square > x:
                j = num - 1
            else:
                i = num + 1
        return j
