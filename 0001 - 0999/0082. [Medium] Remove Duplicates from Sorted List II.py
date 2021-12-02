# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None: 
            return head
        
        ans = prevprev = ListNode(0, head)
        prev = head
        cur = head.next
        removePrev = False
        while cur:             
            if prev.val == cur.val: 
                removePrev = True
                prev.next = cur.next
                cur = cur.next
            elif removePrev:                   
                prevprev.next = cur
                prev = cur  
                cur = prev.next 
                removePrev = False
            else:
                prevprev = prevprev.next
                prev = prev.next
                cur = cur.next
        
        if removePrev: 
            prevprev.next = None
        
        return ans.next
