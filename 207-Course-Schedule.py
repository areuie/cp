class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # how many nodes point to curr
        # zero init list of courses
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)] # 2d adj list of courses

        #init indegree, go to each prereq and add 1 to each 2nd
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1

        queue = deque()
        # try to get 0s first, append to queue
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        #lowest and then reduce the indegree of nearby
        nodesVisited = 0
        while queue:
            # get the node
            node = queue.popleft()
            # increase nodes visited
            nodesVisited+=1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return nodesVisited == numCourses


        


            
        