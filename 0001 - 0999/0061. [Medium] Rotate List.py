# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: 
            return None 
        
        arr = []
        
        while head: 
            arr.append(head)
            
            head = head.next
            
        n = len(arr)
        
        k = k % n 
        
        arr = arr[n - k: ] + arr[: n - k]
        
        for i in range(n - 1):
            arr[i].next = arr[i + 1]
            
        arr[-1].next = None 
        
        return arr[0]
            
        
            
            
