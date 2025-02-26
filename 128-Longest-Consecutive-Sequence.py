class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)

        maxLen = 0
        for num in seq:
            curLen = 0
            if num - 1 not in seq:
                curLen = 1
                i = num

                while i + 1 in seq:
                    curLen+=1
                    i+=1
            maxLen = max(maxLen, curLen)
        return maxLen

