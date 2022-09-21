# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        ans = cur = ListNode(0)
        
        while list1 and list2: 
            val1 = list1.val 
            val2 = list2.val
            
            if val1 < val2: 
                cur.next = ListNode(val1)
                list1 = list1.next 
            else: 
                cur.next = ListNode(val2)
                list2 = list2.next 
                
            cur = cur.next
                
        cur.next = list1 if list1 else list2 
        
        return ans.next
            
                
