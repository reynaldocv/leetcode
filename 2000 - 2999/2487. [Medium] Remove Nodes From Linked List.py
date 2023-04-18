# https://leetcode.com/problems/remove-nodes-from-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            ans = None 
            
            while node: 
                ans = ListNode(node.val, ans)
                
                node = node.next
                
            return ans 
        
        reverse = helper(head)
        
        prev = 0 
        
        ans = cur = ListNode(0)
        
        while reverse: 
            if reverse.val >= prev: 
                cur.next = ListNode(reverse.val)
                
                prev = reverse.val 
                cur = cur.next
                
            reverse = reverse.next 
            
        return helper(ans.next)
