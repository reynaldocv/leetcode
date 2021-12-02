# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = evenList = ListNode(0)
        odd = oddList = ListNode(0)
        turn = True
        while (head):
            if turn: 
                evenList.next = ListNode(head.val)
                evenList = evenList.next
                turn = not turn
            else: 
                oddList.next = ListNode(head.val)
                oddList = oddList.next
                turn = not turn 
            head = head.next
            
        evenList.next = odd.next
        
        return even.next
        
        
