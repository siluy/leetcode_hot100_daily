#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # if self.next == None:
        #     return True
        # value = []
        # cur = head
        # while cur:
        #     value.append(cur.val)
        #     cur = cur.next
        # i, j = 0, len(value) - 1
        # while i < j:
        #     if value[i] != value[j]:
        #         return False
        #     i += 1
        #     j -= 1
        # return True
        if not head or not head.next:
            return True
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second = prev
        p1, p2 = head, second
        res = True
        while p2:
            if p1.val != p2.val:
                res = False
                break
            p1 = p1.next
            p2 = p2.next
        return res
            
# @lc code=end

