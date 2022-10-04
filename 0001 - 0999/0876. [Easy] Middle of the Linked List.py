# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0 
        
        arr = []
        
        while head:
            arr.append(head)
            
            head = head.next
            n += 1 
            
        return arr[n//2]
            
        
        
