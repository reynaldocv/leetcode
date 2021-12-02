# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        ans = l3 = ListNode(0)
        aux = 0
        while  l1 or l2: 
            aux1 = l1.val if l1 else 0
            aux2 = l2.val if l2 else 0
            aux3 = aux1 + aux2 + aux
            if aux3 >= 10: 
                aux = 1
                aux3 = aux3 % 10
            else: 
                aux = 0
            l3.next = ListNode(aux3)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            l3 = l3.next
        if aux == 1: 
            l3.next = ListNode(1)
        return ans.next
            
            
        
