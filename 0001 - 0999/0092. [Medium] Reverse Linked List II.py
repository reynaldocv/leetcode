# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None: return None
        ans = prev = ListNode(0, head)
        middle = ListNode(0)        
        post = None
        position = 1
        while head: 
            if left <= position <= right: 
                middle.next = ListNode(head.val, middle.next)
            if position == left: 
                prev.next = None                
            if position == right: 
                post = head.next
                head.next = None
            position += 1
            head = head.next
            if prev.next:
                prev = prev.next
      
        prev.next = middle.next
        while middle.next: 
            middle = middle.next
        middle.next = post
        
        return ans.next
