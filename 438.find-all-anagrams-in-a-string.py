#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # m, n = len(s), len(p)
        # if n > m:
        #     return []
        # res = []
        # cntp = [0]*26
        # cntw = [0]*26
        # base = ord('a')
        # for ch in p:
        #     cntp[ord(ch)-base] += 1
        # for i in range(n):
        #     cntw[ord(s[i])-base] += 1
        # if cntw == cntp:
        #     res.append(0)
        # for i in range(n, m):
        #     cntw[ord(s[i])-base] += 1
        #     cntw[ord(s[i-n])-base] -= 1
        #     if cntp == cntw:
        #         res.append(i-n+1)
        # return res
        m, n = len(s), len(p)
        if n > m:
            return []
        res = []
        cntp = [0]*26
        cntw = [0]*26
        base = ord('a')
        for ch in p:
            cntp[ord(ch) - base] += 1
        for i in range(n):
            cntw[ord(s[i]) - base] += 1
        if cntp == cntw:
            res.append(0)
        for i in range(n,m):
            cntw[ord(s[i]) - base] += 1
            cntw[ord(s[i - n]) - base] -= 1
            if cntp == cntw:
                res.append(i-n+1)
        return res
# @lc code=end

