# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n = 0 
        cur = head
        while head: 
            n += 1
            head = head.next
        
        if n == 0: 
            return head
        
        k = (n - k) % n
        tail = prev = ListNode(0, cur)
        head = cur
        while k >= 1: 
            prev = prev.next
            head = head.next
            k -= 1            
        prev.next = None
        
        ans = head
        while head.next: 
            head = head.next
        head.next = tail.next
    
        return ans
            
            
