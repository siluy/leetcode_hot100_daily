#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # num_sorted = sorted(nums)
        # return num_sorted[-k]
        # target = len(nums) - k

        # def partition(l: int, r: int) -> int:
        #     pivot_idx = random.randint(l, r)
        #     nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
        #     pivot = nums[r]
        #     i = l
        #     for j in range(l, r):
        #         if nums[j] < pivot:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i += 1
        #     nums[i], nums[r] = nums[r], nums[i]
        #     return i
        
        # l, r = 0, len(nums) - 1
        # while True:
        #     p = partition(l, r)
        #     if p == target:
        #         return nums[p]
        #     elif p < target:
        #         l = p + 1
        #     else:
        #         r = p - 1
        n = len(nums)
        target = n - k  # 第 target 小

        l, r = 0, n - 1
        while l <= r:
            pivot = nums[random.randint(l, r)]
            # 三向分区
            lt, i, gt = l, l, r
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:  # == pivot
                    i += 1
            # 现在:
            # [l, lt-1] < pivot
            # [lt, gt] == pivot
            # [gt+1, r] > pivot
            if target < lt:
                r = lt - 1
            elif target > gt:
                l = gt + 1
            else:
                return nums[lt]  # pivot 值
        return -1  # 理论不会到这里
# @lc code=end

