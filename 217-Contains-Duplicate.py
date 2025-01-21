class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = dict()
        for i in nums:
            if i not in ans:
                ans[i] = 1
            else: 
                ans[i] += 1
            if ans[i] == 2:
                return True
        return False
        