#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(1, n+1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
# @lc code=end

