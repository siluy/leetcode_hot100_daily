#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # people.sort(key=lambda x: (-x[0], x[1]))
        # res: List[List[int]] = []
        # for h, k in people:
        #     res.insert(k, [h, k])
        # return res
        people.sort(key=lambda x: (-x[0], x[1]))
        res: List[List[int]] = []
        for h, k in people:
            res.insert(k, [h, k])
        return res
# @lc code=end

