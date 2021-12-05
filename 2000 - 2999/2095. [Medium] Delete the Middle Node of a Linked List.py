# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur: 
            arr.append(cur)
            cur = cur.next
            
        n = len(arr)
        
        if n == 1: 
            return None
        elif n == 2: 
            return ListNode(head.val)
            
        mid = n//2
        
        arr[mid - 1].next = arr[mid + 1]
        
        return arr[0]
