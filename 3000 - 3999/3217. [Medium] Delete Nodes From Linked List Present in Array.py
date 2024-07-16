# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        ans = cur = ListNode(0)
        
        seen = {num for num in nums}
        
        while head: 
            if head.val not in seen: 
                cur.next = ListNode(head.val)
                
                cur = cur.next 
                
            head = head.next 
            
        return ans.next
        
