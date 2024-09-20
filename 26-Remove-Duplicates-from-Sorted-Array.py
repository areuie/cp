class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        p = 0
        for r, rVal in enumerate(nums):
            if r == 0:
                continue
            if nums[p] != rVal:
                p+=1
                nums[p] = rVal
        return p+1