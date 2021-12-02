# https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        cur = list1
        i = 0 
        while cur:                 
            if i == a - 1: 
                start = cur
            elif i == b + 1: 
                end = cur
                
            cur = cur.next            
            i += 1    
        
        start.next = list2
        
        while list2.next: 
            list2 = list2.next
            
        list2.next = end
        
        return list1
            
        
