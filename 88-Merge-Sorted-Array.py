class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        \\\
        Do not return anything, modify nums1 in-place instead.
        \\\
        pI, p1, p2 = m + n -1, m -1, n -1
        while pI >= 0:
            if p2 < 0 or p1 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[pI] = nums1[p1]
                p1-=1
            elif p1 < 0 or p2 >= 0 and nums1[p1] <= nums2[p2]:
                nums1[pI] = nums2[p2]
                p2-=1
            pI-=1
            
