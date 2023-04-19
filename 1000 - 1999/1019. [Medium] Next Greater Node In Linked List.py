# https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        
        while head: 
            arr.append(head.val)
            
            head = head.next 
            
        n = len(arr)
        
        ans = [0 for _ in range(n)]
        
        stack = []
        
        for (i, num) in enumerate(arr):
            while stack and stack[-1][0] < num: 
                (_, idx) = stack.pop() 
                
                ans[idx] = num 
            
            stack.append((num, i))
            
        return ans
            
        
        
        
