class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for m, target in enumerate(nums):
            l, r = m + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -target:
                    ans.add((nums[l], nums[r], target))
                    l+=1
                    r-=1
                elif nums[l] + nums[r] < -target:
                    l+=1
                else:
                    r-=1
                
        return ans


        