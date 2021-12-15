# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None
        
        nodes = []
        n = 0
        while head:
            nodes.append(head)
            n += 1 
            head = head.next
        
        nodes.sort(key = lambda item: item.val)
        
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]
            
        nodes[-1].next = None
        
        return nodes[0]
            
        
        
