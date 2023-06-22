# https://leetcode.com/problems/merge-nodes-in-between-zeros/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = cur = ListNode(0)
        
        aSum = 0 
        
        while head: 
            if head.val == 0: 
                if aSum != 0: 
                    cur.next = ListNode(aSum)
                    
                    cur = cur.next
                    
                aSum = 0 
                    
            else: 
                aSum += head.val
                
            head = head.next
                
        return ans.next 
