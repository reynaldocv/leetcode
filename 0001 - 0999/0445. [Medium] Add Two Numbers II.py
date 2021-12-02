# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(l1):
            ans = None
            while l1: 
                ans = ListNode(l1.val, ans)
                l1 = l1.next
            
            return ans
        
        revL1, revL2 = reverse(l1), reverse(l2)
        
        ans = cur = ListNode(0, None)
        
        
        aux = 0
        while revL1 or revL2: 
            val1 = revL1.val if revL1 else 0 
            val2 = revL2.val if revL2 else 0 
            
            val3 = (val1 + val2 + aux) % 10
            aux = (val1 + val2 + aux) // 10
            
            cur.next = ListNode(val3)
            
            revL1 = revL1.next if revL1 else None
            revL2 = revL2.next if revL2 else None
            
            cur = cur.next
            
        if aux != 0:
            cur.next = ListNode(aux)
            
        return reverse(ans.next)
        
        
