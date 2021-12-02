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
            print(head.val)
            if head not in seen: 
                seen[head] = True
            else: 
                return head
            head = head.next
        
        return None
    
class Solution2:
    def detectCycle(self, head: ListNode) -> ListNode:
        once = head
        twice = head
        while twice and twice.next: 
            once = once.next
            twice = twice.next.next
            if once == twice: 
                start = head
                while start != once: 
                    start = start.next
                    once = once.next
                    
                return start
        
        return None
        
      
