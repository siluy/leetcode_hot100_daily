#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1
        ans = 0
        for x in nums:
            prefix += x
            ans += freq[prefix - k]
            freq[prefix] += 1
        return ans
# @lc code=end

