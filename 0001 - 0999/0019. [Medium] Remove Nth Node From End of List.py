# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        
        while head: 
            arr.append(head)
            
            head = head.next 
            
        m = len(arr)
        
        arr.pop(m - n)
        
        if not arr: 
            return None 
        
        for i in range(m - 2):
            arr[i].next = arr[i + 1]
            
        arr[-1].next = None 
        
        return arr[0]
            

class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m = 0 
        
        cur = head 
        
        while cur: 
            cur = cur.next 
        
            m += 1 
            
        k = m - n 
        
        ans = head = ListNode(0, head)
        
        while k >= 0: 
            if k == 0: 
                head.next = head.next.next
                
                break 
                
            head = head.next             
            k -= 1
            
        return ans.next 
                
