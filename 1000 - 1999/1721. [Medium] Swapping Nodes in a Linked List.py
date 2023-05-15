# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: 
            return None 
        
        arr = []
        
        while head: 
            arr.append(head)
            
            head = head.next 
            
        n = len(arr)
        
        arr[k - 1].val , arr[n - k].val = arr[n - k].val, arr[k - 1].val 
        
        return arr[0]
        
            
            
            
    
