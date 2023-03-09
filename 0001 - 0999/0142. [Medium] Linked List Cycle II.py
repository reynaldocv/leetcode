# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = {}
        
        while head:             
            if head not in seen: 
                seen[head] = True
            
            else: 
                return head
            
            head = head.next
        
        return None

class Solution2:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
            
            if slow == fast: 
                fast = head
                
                while slow != fast: 
                    slow = slow.next
                    fast = fast.next
                    
                return slow 
                
        return None
        
      
