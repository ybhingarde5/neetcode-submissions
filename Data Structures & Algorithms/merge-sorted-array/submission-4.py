class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i,j = m - 1, n - 1
        last = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j-=1
            last -= 1

        # while j >= 0:
        #     nums1[last] = nums2[j]
        #     j-=1
        #     last-=1












        # nums1[m:] = nums2[:n]
        
        # i = len(nums1) - 1
        # while i > 0:
        #     j = 0
        #     while j < i:
        #         if nums1[j] > nums1[j+1]:
        #             nums1[j], nums1[j+1] = nums1[j+1], nums1[j]
        #         j+=1
        #     i-=1
        


