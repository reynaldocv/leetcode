# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-inf)
        ans.next = ListNode(head.val)
        
        node = head.next
        while node: 
            prev = ans
            cur = ans.next
            insert = True
            while cur: 
                if prev.val <= node.val <= cur.val:
                    insert = False
                    prev.next = ListNode(node.val)
                    prev.next.next = cur
                    break
                else:            
                    prev = prev.next            
                    cur = cur.next
            if insert: 
                prev.next = ListNode(node.val)
                prev.next.next = None
            node = node.next    
        return ans.next
                    
        
        
        
