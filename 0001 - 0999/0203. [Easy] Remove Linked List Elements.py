# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ans = prev = ListNode(inf, head)
        while head: 
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return ans.next
        
