#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return head
        # n = 0
        # cur = head
        # while cur:
        #     n += 1
        #     cur = cur.next
        
        # def split(h, size):
        #     if not h:
        #         return None
        #     for _ in range(size - 1):
        #         if not h.next:
        #             break
        #         h = h.next
        #     second = h.next
        #     h.next = None
        #     return second

        # def merge(l1, l2):
        #     dummy = tail = ListNode(0)
        #     while l1 and l2:
        #         if l1.val <= l2.val:
        #             tail.next, l1 = l1, l1.next
        #         else:
        #             tail.next, l2 = l2, l2.next
        #         tail = tail.next
        #     tail.next = l1 if l1 else l2
        #     while tail.next:
        #         tail = tail.next
        #     return dummy.next, tail
        
        # dummy = ListNode(0, head)
        # size = 1
        # while size < n:
        #     prev = dummy
        #     cur = dummy.next
        #     while cur:
        #         left = cur
        #         right = split(left, size)
        #         cur = split(right, size)
        #         merged_head, merged_tail = merge(left, right)
        #         prev.next = merged_head
        #         prev = merged_tail
        #     size <<= 1
        # return dummy.next
        if not head or not head.next:
            return head
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        def split(h, size):
            if not h:
                return None
            for _ in range(size - 1):
                if not h.next:
                    break
                h = h.next
            second = h.next
            h.next = None
            return second
        
        def merge(l1, l2):
            dummy = tail = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next, l1 = l1, l1.next
                else:
                    tail.next, l2 = l2, l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            while tail.next:
                tail = tail.next
            return dummy.next, tail
        
        dummy = ListNode(0, head)
        size = 1
        while size < n:
            prev = dummy
            cur = dummy.next
            while cur:
                left = cur
                right = split(left, size)
                cur = split(right, size)
                merged_head, merged_tail = merge(left, right)
                prev.next = merged_head
                prev = merged_tail
            size <<= 1
        return dummy.next
# @lc code=end

