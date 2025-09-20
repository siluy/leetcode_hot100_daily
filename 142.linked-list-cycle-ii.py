#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow is fast:
        #         break
        # else:
        #     return None
        
        # slow = head
        # while slow is not fast:
        #     slow = slow.next
        #     fast = fast.next
        # return slow
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow
# @lc code=end

