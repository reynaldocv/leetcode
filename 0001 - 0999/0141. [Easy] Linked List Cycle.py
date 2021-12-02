# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dic = {}
        while head != None and head not in dic : 
            dic[head] = True
            head = head.next
        if head in dic: 
            return True
        else: 
            return False
        
