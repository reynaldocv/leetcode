# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0 
        cur = head
        while cur: 
            cur = cur.next
            n += 1
        
        start = min(k, n - k + 1)
        end = max(k, n - k + 1)
        val1, val2 = 0, 0
        
        cur = head
        i = 1
        while cur: 
            if i == start: 
                val1 = cur.val
            if i == end: 
                val2 = cur.val
            cur = cur.next
            i +=1
            
        cur = head
        i = 1
        while cur: 
            if i == start: 
                cur.val = val2
            if i == end: 
                cur.val = val1
            cur = cur.next
            i +=1
        
        return head
            
            
            
    
