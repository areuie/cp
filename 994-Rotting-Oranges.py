class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        visited = set()
        freshOranges = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) in visited:
                    continue
                if grid[r][c] == 2:
                    queue.append((r,c, 0))
                if grid[r][c] == 1:
                    freshOranges += 1

        res = 0
        while queue:
            print(queue)
            r, c, t = queue.popleft()
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0 or (r,c) in visited:
                continue
            visited.add((r,c))
            if grid[r][c] == 1:
                freshOranges -= 1
            queue.append((r+1, c, t + 1))
            queue.append((r-1, c, t + 1))
            queue.append((r, c+1, t + 1))
            queue.append((r, c-1, t + 1))
            res = t
        
        return res if freshOranges == 0 else -1
