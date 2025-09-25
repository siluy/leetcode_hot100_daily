#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for w in strs:
            cnt = [0] * 26
            for ch in w:
                cnt[ord(ch) - ord('a')] += 1
            groups[tuple(cnt)].append(w)
        return list(groups.values())
# @lc code=end

