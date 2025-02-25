class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        \\\
        Do not return anything, modify nums1 in-place instead.
        \\\
        l = m - 1
        r = n - 1
        for i in range(m+n-1, -1, -1):
            if r < 0:
                continue
            val = 0
            if l >= 0 and nums1[l] >= nums2[r]:
                val = nums1[l]
                l-=1
            else:
                val = nums2[r]
                r-=1
            nums1[i] = val
        
        
