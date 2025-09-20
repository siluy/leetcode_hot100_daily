#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, c in freq.items():
            buckets[c].append(val)
        res = []
        for c in range(len(nums), 0, -1):
            if buckets[c]:
                res.extend(buckets[c])
                if len(res) >= k:
                    return res[:k]
        return res
# @lc code=end

