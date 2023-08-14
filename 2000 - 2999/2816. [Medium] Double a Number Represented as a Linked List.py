# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head):
            ans = None 
            
            while head: 
                ans = ListNode(head.val, ans)
                
                head = head.next
                
            return ans 
        
        reverse = helper(head)
        
        ans = cur = ListNode(0)
        aux = 0 
        
        while reverse != None or aux != 0: 
            unit = reverse.val if reverse else 0
            
            total = 2*unit + aux
            
            cur.next = ListNode(total % 10)            
            aux = total // 10
            
            cur = cur.next            
            reverse = reverse.next if reverse else None
                       
        return helper(ans.next)
