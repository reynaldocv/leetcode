# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n, m = 0, 0
        
        cur = headA
        while cur: 
            n += 1 
            cur = cur.next
        
        cur = headB
        while cur: 
            m += 1 
            cur = cur.next
            
        while n != m:             
            if n > m: 
                headA = headA.next
                n -= 1
            elif m > n:
                headB = headB.next
                m -= 1
            
        while headA != headB: 
            headA = headA.next
            headB = headB.next

        return headA
