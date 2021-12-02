# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(arr, start, end):
            for i in range(k//2):
                arr[start + i], arr[end - i] = arr[end - i], arr[start + i]
        
        cur = head
        stack = []        
        while cur: 
            stack.append(cur)
            cur = cur.next
        
        n = len(stack)
        for start in range(0, n, k):
            end = start + k - 1
            if end < n: 
                reverse(stack, start, end)
                
        for i in range(n - 1):
            stack[i].next = stack[i + 1]
            
        stack[-1].next = None
        
        return stack[0]
