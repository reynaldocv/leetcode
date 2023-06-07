# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        
        while head: 
            insort(arr, head, key = lambda item: item.val)
            
            head = head.next
            
        n = len(arr)
        
        for i in range(n - 1):
            arr[i].next = arr[i + 1]
            
        arr[-1].next = None 
        
        return arr[0]
        
            
