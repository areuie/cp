class UnionFind:
    def __init__(self, size: int) -> None:
        self.group = [0] * size
        self.rank = [0] * size
        #height is 0
        
        # init where it points to itself
        for i in range(size):
            self.group[i] = i
      
    def find(self, node: int) -> int:
        if self.group[node] != node: # if parent is
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1: int, node2: int) -> bool:
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        # node1 and node2 already belong to same group.
        if group1 == group2:
            return False

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1

        return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # sort by closest
        n = len(points)
        all_edges = []

        for currN in range(n):
            for nextN in range(currN + 1, n):
                weight = abs(points[nextN][0] - points[currN][0]) + abs(points[nextN][1] - points[currN][1]) 
                all_edges.append((weight, currN, nextN))
        
        all_edges.sort()
        uf = UnionFind(n)

        mst_cost = 0
        edges_used = 0

        for weight, node1, node2 in all_edges:
            if uf.join(node1, node2):
                mst_cost += weight
                edges_used = 0
                if edges_used == n - 1:
                    break
                

        return mst_cost