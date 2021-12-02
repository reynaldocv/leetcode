# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        pointers = []
        while (head):
            pointers.append(head)
            head = head.next
            
        return pointers[len(pointers)//2]
        
