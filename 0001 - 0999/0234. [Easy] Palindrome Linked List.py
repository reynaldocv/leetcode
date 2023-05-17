# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans = ""
        
        while head: 
            ans += str(head.val)
            
            head = head.next 
            
        return ans == ans[:: -1]

class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = None 
        
        cur = head
        
        while cur: 
            reverse = ListNode(cur.val, reverse)
            
            cur = cur.next
            
        while head and reverse: 
            if head.val != reverse.val: 
                return False 
            
            head = head.next 
            reverse = reverse.next 
            
        return True 
            
        
        
