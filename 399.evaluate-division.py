#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from typing import List
from collections import deque, defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # graph = defaultdict(list)
        # for (a, b), v in zip(equations, values):
        #     graph[a].append((b, v))
        #     graph[b].append((a, 1.0 / v))
        # def bfs(src: str, dst: str) -> float:
        #     if src not in graph or dst not in graph:
        #         return -1.0
        #     if src == dst:
        #         return 1.0
        #     q = deque([(src, 1.0)])
        #     seen = {src}
        #     while q:
        #         node, val = q.popleft()
        #         if node == dst:
        #             return val
        #         for nxt, w in graph[node]:
        #             if nxt not in seen:
        #                 seen.add(nxt)
        #                 q.append((nxt, val * w))
        #     return -1.0
        # return [bfs(a, b) for a, b in queries]
        graph = defaultdict(list)
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1.0 / v))
        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            q = deque([(src, 1.0)])
            seen = {src}
            while q:
                node, val = q.popleft()
                if node == dst:
                    return val
                for nxt, w in graph[node]:
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, w * val))
            return -1.0
        return [bfs(a, b) for a, b in queries]
# @lc code=end

