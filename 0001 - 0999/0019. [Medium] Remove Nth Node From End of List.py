# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = 0
        ans = prev = ListNode(0, head)
        cur = head
        while head: 
            l += 1
            head = head.next
        n = l - n   
        
        while cur: 
            if n != 0:
                prev = prev.next
                cur = cur.next
            else: 
                prev.next = cur.next
                break                 
            n -= 1
        return ans.next
                
            
