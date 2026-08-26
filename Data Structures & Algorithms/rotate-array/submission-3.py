class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        bigK = k%n
        nums[:] = nums[n-bigK:] + nums[:n-bigK]


        # lastElem = 0
        # changed = False
        # for _ in range(k):
        #     for i in range(len(nums)-1, -1, -1):
        #         if not changed:
        #             lastElem = nums[-1]
        #             changed = True
        #         nums[i] = nums[i-1]
        #     nums[0] = lastElem
        #     changed = False
        # return nums






























        # n = len(nums)
        # k = k % n

        # def reverse(start, stop):
        #     while start < stop:
        #         nums[start] , nums[stop] = nums[stop], nums[start]
        #         start+=1
        #         stop-=1
        
        # reverse(0, n-1)
        # reverse(0, k-1)
        # reverse(k, n-1)
