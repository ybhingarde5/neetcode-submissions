# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1

class Solution:
    def guessNumber(self, n: int) -> int:
        i = 0
        j = n

        while i <= j:
            num = i + (j - i) // 2
            ans = guess(num)
            if ans == 0:
                return num
            elif ans == 1:
                i = num + 1
            else:
                j = num - 1
    
             