#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self._st = []
        self._min = []

    def push(self, val: int) -> None:
        self._st.append(val)
        if self._min:
            self._min.append(val if val < self._min[-1] else self._min[-1])
        else:
            self._min.append(val)

    def pop(self) -> None:
        self._st.pop()
        self._min.pop()

    def top(self) -> int:
        return self._st[-1]

    def getMin(self) -> int:
        return self._min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

