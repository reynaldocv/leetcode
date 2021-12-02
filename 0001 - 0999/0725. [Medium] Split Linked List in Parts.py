# https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        n = 0        
        ans = []
       
        while cur: 
            n += 1
            cur = cur.next
        
        quo, res = divmod(n, k)
         
        cur = head
        for i in range(k):
            head = cur
            for j in range(quo + (i < res) - 1):
                if cur: 
                    cur = cur.next
            if cur: 
                cur.next, cur = None, cur.next
            ans.append(head)
    
        return ans
        
