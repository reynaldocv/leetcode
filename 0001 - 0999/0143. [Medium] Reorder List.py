# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """        
        arr = []
        
        while head: 
            arr.append(head)
            
            head = head.next 
            
        ans = []
        
        turn = 1
        
        while arr: 
            if turn: 
                ans.append(arr.pop(0))
            
            else:
                ans.append(arr.pop())
                
            turn = 1 - turn 
            
        n = len(ans)
        
        for i in range(n - 1):
            ans[i].next = ans[i + 1]
            
        ans[-1].next = None 
        
        
            
        
        
        
