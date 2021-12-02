# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        n = 0 
        reverse = None
        cur = head
        while cur: 
            reverse = ListNode(cur.val, reverse)
            cur = cur.next
            n += 1
        
        ans = ListNode(0, head)
        i = 0
        while (i < n//2):
            ans.next = head
            head = head.next
            ans = ans.next
            
            ans.next = reverse
            reverse = reverse.next
            ans = ans.next            
            i += 1
        
        if n % 2 == 0: 
            ans.next = None
        else: 
            ans.next.next = None
    
    
class Solution2:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        cur = head.next
        while cur:
            stack.append(cur)
            cur = cur.next
            
        cur = head
        right = True
        while stack: 
            if right: 
                cur.next = stack.pop()
            else: 
                cur.next = stack.pop(0)
            right = not right
            cur = cur.next
            
        cur.next = None
            
        
        
