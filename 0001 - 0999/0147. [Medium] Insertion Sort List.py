# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        arr = []
        n = 0 
        while head:
            idx = bisect_left(arr, head.val)
            arr.insert(idx, head.val)
            nodes.insert(idx, head)
            head = head.next
            n += 1
            
        for i in range(1, n):
            nodes[i - 1].next = nodes[i]
            
        nodes[-1].next = None
        
        return nodes[0]
            
