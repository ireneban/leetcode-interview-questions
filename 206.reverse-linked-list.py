#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Solution from Discussion: https://leetcode.com/problems/reverse-linked-list/discuss/58127/Python-Iterative-and-Recursive-Solution
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
        
# @lc code=end

