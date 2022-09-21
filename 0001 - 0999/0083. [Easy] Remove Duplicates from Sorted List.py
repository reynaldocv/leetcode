# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = -inf 
        
        ans = cur = ListNode(0)
        
        while head: 
            if head.val != prev: 
                cur.next = ListNode(head.val)
                cur = cur.next
                
            prev = head.val 
                
            head = head.next 
            
        return ans.next
                
            
                
            
