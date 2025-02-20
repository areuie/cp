class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort()
        n = len(citations)

        l, r = 0, n

        while l < r:
            m = (l + r) // 2
            if citations[m] >= n - m:
                r = m
            elif citations[m] < n - m:
                l = m + 1
        
        return n - l