class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)
        
        def merge(left, right):
            i, j = 0,0
            result = []
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    result.append(right[j])
                    j+=1
                else:
                    result.append(left[i])
                    i+=1
            
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        return merge_sort(nums)

        



        # bubble sort
        # end = len(nums)
        # i , j = 0, 1
        # while end > 0:
        #     while j < end:
        #         if nums[j] < nums[i]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #         i+=1
        #         j+=1
        #     i = 0
        #     j = 1
        #     end-=1
        # return nums



        # two pointer sort [selection sirt]
        # n = len(nums)
        # i = 0

        # while i < n:
        #     j = i

        #     while j < n:
        #         if nums[j] < nums[i]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #         j+=1
            
        #     i+=1
        
        # return nums