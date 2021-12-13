# https://leetcode.com/problems/linked-list-components/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:        
        ans = 0 
        prev = False
        while head: 
            if head.val in nums: 
                if prev == False: 
                    ans += 1
                    prev = True
            else: 
                prev = False
                
            head = head.next
            
        return ans
            
 
