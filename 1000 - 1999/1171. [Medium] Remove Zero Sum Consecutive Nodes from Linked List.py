# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = tmp = ListNode(0, head)
        
        seen = {0: tmp}        
        aSum = 0
        
        while head:
            aSum += head.val
            
            seen[aSum] = head
            
            head = head.next
            
        head = tmp
        aSum = 0
        
        while head:
            aSum += head.val
            
            head.next = seen[aSum].next
            
            head = head.next
            
        return ans.next

class Solution2:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = [(0, ListNode(0, head))]
        
        seen = {0}
        prev = 0 
        
        while head:             
            prev += head.val 
            
            if prev in seen: 
                while stack[-1][0] != prev: 
                    tmp = stack.pop() 
                    seen.remove(tmp[0])
                    
            else: 
                seen.add(prev)                
                
                stack.append((prev, head))
                
            stack[-1][1].next = head.next
            head = head.next
                
        return stack[0][1].next
        
        
