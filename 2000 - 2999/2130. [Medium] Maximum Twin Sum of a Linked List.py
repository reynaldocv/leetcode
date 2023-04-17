# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        
        n = 0 
        
        while head: 
            arr.append(head.val)
            
            head = head.next 
            n += 1 
            
        ans = 0 
        
        for i in range(n//2):
            ans = max(ans, arr[i] + arr[n - 1 - i])
            
        return ans 
        
