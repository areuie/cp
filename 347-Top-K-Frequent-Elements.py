class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, val in freq.items():
            heapq.heappush(heap, (-val, key))

        for i in range(k):
            val, key = heapq.heappop(heap)
            res.append(key)

        return res