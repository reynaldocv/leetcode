# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2list(l1, l2):
            ans = cur = ListNode(0)
            while l1 and l2: 
                if l1.val < l2.val: 
                    cur.next = ListNode(l1.val)
                    cur = cur.next
                    l1 = l1.next
                else: 
                    cur.next = ListNode(l2.val)
                    cur = cur.next
                    l2 = l2.next
            
            cur.next = l1 if l1 else l2
            
            return ans.next
        
        n = len(lists)
        
        interval = 1
        while interval < n: 
            for i in range(0, n - interval, interval*2):
                lists[i] = merge2list(lists[i], lists[i + interval])
            interval *= 2
            
        return lists[0] if n > 0 else None
            
            
