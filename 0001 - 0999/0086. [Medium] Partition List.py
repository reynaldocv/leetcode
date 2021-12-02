# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lower = prev = ListNode(0)
        greater = post = ListNode(0)
        cur = head
        while head: 
            if head.val < x: 
                prev.next = ListNode(head.val)
                prev = prev.next
            else: 
                post.next = ListNode(head.val)
                post = post.next
            head = head.next
        
        prev = lower
        while prev.next: 
            prev = prev.next
        
        prev.next = greater.next
        
        return lower.next
        
        
        
