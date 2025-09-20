#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range (numCourses)]
        indeg = [0]*numCourses
        for a,b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1
        q = deque([i for i in range(numCourses) if indeg[i]==0])
        taken = 0
        while q:
            u = q.popleft()
            taken += 1
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return taken == numCourses
# @lc code=end

