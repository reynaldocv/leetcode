# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = tmp = ListNode(0, head)
        
        seen = {0: tmp}        
        aSum = 0
        
        while head:
            aSum += head.val
            
            seen[aSum] = head
            
            head = head.next
            
        head = tmp
        aSum = 0
        
        while head:
            aSum += head.val
            
            head.next = seen[aSum].next
            
            head = head.next
            
        return ans.next
        
