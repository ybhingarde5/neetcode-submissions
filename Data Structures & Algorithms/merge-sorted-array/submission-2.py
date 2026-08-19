class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i-m]
        
        i = len(nums1) - 1
        while i > 0:
            j = 0
            while j < i:
                if nums1[j] > nums1[j+1]:
                    nums1[j], nums1[j+1] = nums1[j+1], nums1[j]
                j+=1
            i-=1
        


