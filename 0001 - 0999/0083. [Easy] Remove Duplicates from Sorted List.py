# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        ans = cur = ListNode(0)
        value = inf
        while head: 
            if head.val != value:                 
                value = head.val 
                cur.next = ListNode(head.val)
                cur = cur.next
            head = head.next
        return ans.next
                
            
                
            
