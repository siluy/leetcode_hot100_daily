#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordSet = set(wordDict)
        # if not wordSet:
        #     return False
        # n = len(s)
        # min_len = min(len(w) for w in wordSet)
        # max_len = max(len(w) for w in wordSet)
        # dp = [False] * (n + 1)
        # dp[0] = True
        # for i in range(1, n + 1):
        #     for l in range(min_len, max_len + 1):
        #         j = i - l
        #         if j < 0:
        #             break
        #         if dp[j] and s[j:i] in wordSet:
        #             dp[i] = True
        #             break
        # return dp[n]
        wordSet = set(wordDict)
        if not wordSet:
            return False
        n = len(s)
        min_len = min(len(w) for w in wordSet)
        max_len = max(len(w) for w in wordSet)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for l in range(min_len, max_len + 1):
                j = i - l
                if j < 0:
                    break
                if dp[j] and s[i:j] in wordSet:
                    dp[i] = True
                    break
        return dp[n]
# @lc code=end

