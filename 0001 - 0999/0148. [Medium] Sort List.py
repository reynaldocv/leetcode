# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def divide(head, n):
            if n <= 1: 
                return head
            else: 
                m = n//2
                i = 1
                left = cur = head
                right = head.next
                while i < m: 
                    cur = cur.next
                    right = right.next
                    i += 1                    
                cur.next = None
                
                left = divide(left, m)
                right = divide(right, n - m)
                
                ans = cur = ListNode(0)
                while left and right: 
                    if left.val < right.val:
                        cur.next = ListNode(left.val)
                        left = left.next
                    else: 
                        cur.next = ListNode(right.val)
                        right = right.next
                    cur = cur.next
                    
                cur.next = left if left else right
                
                return ans.next
        
        n = 0 
        cur = head
        while cur:
            n += 1 
            cur = cur.next
    
        return divide(head, n)
