#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_cnt = max(freq.values())
        max_count = sum(1 for v in freq.values() if v == max_cnt)
        frame = (max_cnt - 1) * (n + 1) + max_count
        return max(len(tasks), frame)
# @lc code=end

