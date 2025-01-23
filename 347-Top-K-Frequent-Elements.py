class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        hashMap = {}
        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1
        
        for key, val in hashMap.items():
            heapq.heappush(heap,(-val, key))

        res = []
        for i in range(k):
            val, key = heapq.heappop(heap)
            res.append(key)
        
        return res