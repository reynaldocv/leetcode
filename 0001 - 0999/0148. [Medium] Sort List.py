# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None 
        
        arr = []
        
        while head: 
            arr.append(head)
            
            head = head.next 
            
        arr.sort(key = lambda item: item.val)
        
        n = len(arr)
        
        for i in range(n - 1):
            arr[i].next = arr[i + 1]
            
        arr[-1].next = None 
        
        return arr[0]
        
            
        
        
