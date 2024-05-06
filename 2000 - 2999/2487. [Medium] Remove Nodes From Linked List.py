# https://leetcode.com/problems/remove-nodes-from-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        while head: 
            val = head.val 
            
            while stack and stack[-1].val < val: 
                stack.pop() 
                
            stack.append(head)
            head = head.next 
            
        m = len(stack)
        
        for i in range(m - 1):
            stack[i].next = stack[i + 1]
            
        return stack[0]
