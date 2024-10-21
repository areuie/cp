class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        #create a min and max heap, and find the abs diff.
        # do a sliding window and move l up if diff greater than limit
        # keep track of longest subarray
        minheap = []
        maxheap = []
        res = 0
        l = 0
        for r in range(len(nums)):
            heapq.heappush(minheap, (nums[r], r))
            heapq.heappush(maxheap, (-nums[r], r))
            while abs(minheap[0][0] - -maxheap[0][0]) > limit:
                while minheap[0][1] <= l:
                    heapq.heappop(minheap)
                while maxheap[0][1] <= l:
                    heapq.heappop(maxheap)
                l+=1
            res = max(res, r - l + 1)
        return res
            


