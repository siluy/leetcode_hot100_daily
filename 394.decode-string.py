#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = []
        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == '[':
                stack.append(("".join(cur_str), cur_num))
                cur_str = []
                cur_num = 0
            elif ch == ']':
                prev_str, k = stack.pop()
                cur_str = [prev_str + "".join(cur_str) * k]
            else:
                cur_str.append(ch)
        return "".join(cur_str)
# @lc code=end

