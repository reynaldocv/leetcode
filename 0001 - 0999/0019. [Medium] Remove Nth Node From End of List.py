# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m = 0 
        
        arr = []
        
        while head:
            arr.append(head)
            m += 1  
            
            head = head.next
            
        n = m - n 
        
        arr.pop(n)
        
        if not arr: 
            return None 
        
        for i in range(m - 2):
            arr[i].next = arr[i + 1]
            
        arr[-1].next = None
        
        return arr[0]

class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(node):
            ans = None 

            while node: 
                ans = ListNode(node.val, ans)

                node = node.next 
                
            return ans 

        m = 1 
        
        ans = prev = ListNode(0, helper(head))
        cur = prev.next
        
        while m <= n: 
            if m == n: 
                prev.next = cur.next                
                
            prev = prev.next 
            cur = cur.next
            
            m += 1             
            
        return helper(ans.next)            
