# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            ans = None 
            
            while node:
                ans = ListNode(node.val, ans)
                
                node = node.next
                
            return ans 
        
        l1 = helper(l1)
        l2 = helper(l2)
        
        ans = cur = ListNode(0)
        
        aux = 0 
        
        while l1 or l2 or aux != 0: 
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0 
            
            aSum = (val1 + val2 + aux) % 10 
            
            aux = (val1 + val2 + aux)//10
            
            cur.next = ListNode(aSum)
            
            cur = cur.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
            
        return helper(ans.next)
            
            
            
            
        
