# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr = []
        
        while head: 
            arr.append(head)
            
            head = head.next 
            
        n = len(arr)
        
        arr = arr[: left - 1] + arr[left - 1: right][:: -1] + arr[right: ]
        
        for i in range (n - 1):
            arr[i].next = arr[i + 1]
            
        arr[-1].next = None 
        
        return arr[0]
