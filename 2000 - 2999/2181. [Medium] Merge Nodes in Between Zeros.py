# https://leetcode.com/problems/merge-nodes-in-between-zeros/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        arr = []
        prefix = 0 
        head = head.next
        
        ans = node = ListNode(0)
        
        while head: 
            if head.val == 0: 
                node.next = ListNode(prefix)
                node = node.next
                prefix = 0
            else: 
                prefix += head.val
                
            head = head.next
            
        
        return ans.next
