# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        ans = cur = ListNode(0)                
        while l1 and l2: 
            if l1.val < l2.val:                
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else: 
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
      
        if l1: 
            cur.next = l1
        else: 
            cur.next = l2
            
        return ans.next
            
                
