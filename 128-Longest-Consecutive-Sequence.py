class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxLen = 0

        for i in hashSet:
            if i - 1 not in hashSet:
                currLen = 1
                currVal = i

                while currVal + 1 in hashSet:
                    currLen += 1
                    currVal += 1
                
                maxLen = max(maxLen, currLen)
        
        return maxLen

