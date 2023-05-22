# https://leetcode.com/problems/partition-list/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lower = prev = ListNode(0)
        greater = post = ListNode(0)
        
        cur = head
        
        while head: 
            if head.val < x: 
                prev.next = ListNode(head.val)                
                prev = prev.next
                
            else: 
                post.next = ListNode(head.val)                
                post = post.next
                
            head = head.next
        
        prev.next = greater.next
        
        return lower.next

class Solution2:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: 
            return None 
        
        lower = []
        greater = []
        
        while head: 
            if head.val < x: 
                lower.append(head)
                
            else: 
                greater.append(head)
                
            head = head.next 
            
        arr = lower + greater 
        
        n = len(arr)
        
        for i in range(n - 1):
            arr[i].next = arr[i + 1]
            
        arr[-1].next = None 
    
        return arr[0]
        
        
