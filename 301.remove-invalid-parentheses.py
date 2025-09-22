#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(t):
            bal = 0
            for ch in t:
                if ch == '(':
                    bal += 1
                elif ch == ')':
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0
        res = []
        visited = {s}
        q = deque([s])
        found = False
        while q:
            cur = q.popleft()
            if is_valid(cur):
                res.append(cur)
                found = True
            if found:
                continue
            for i, ch in enumerate(cur):
                if ch not in ('(', ')'):
                    continue
                if i > 0 and cur[i] == cur[i-1]:
                    continue
                nxt = cur[:i] + cur[i+1:]
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        return res

# @lc code=end

