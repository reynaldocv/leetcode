# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head 
        
        counter = defaultdict(lambda: 0)
        
        while cur: 
            counter[cur.val] += 1 
            
            cur = cur.next 
            
        ans = cur = ListNode(0)
        
        while head: 
            if counter[head.val] == 1: 
                cur.next = ListNode(head.val)
                
                cur = cur.next
                
            head = head.next 
            
        return ans.next
    
class Solution2:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:            
        ans = cur = ListNode(0)
        
        prev = inf 
        
        counter = 2 
        
        while head: 
            if head.val != prev: 
                if counter == 1: 
                    cur.next = ListNode(prev)
                    
                    cur = cur.next 
                    
                prev = head.val                 
                counter = 1 
                    
            else: 
                counter += 1 
                
            head = head.next
            
        if counter == 1: 
            cur.next = ListNode(prev)
            
        return ans.next
        
