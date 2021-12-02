# https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        n = 0 
        cur = head
        while cur: 
            n += 1
            cur = cur.next
            
        ans = [0]*n
        
        FILO = [(head.val, 0)]
        i = 1
        head = head.next
        while head: 
            val = head.val 
            while FILO and val > FILO[-1][0]:
                (_, position) = FILO.pop()
                ans[position] = val
            FILO.append((val, i))
            i += 1
            head = head.next
            
        return ans
            
class Solution2:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:        
        FILO = []
        i = 0        
        ans = []
        
        while head: 
            val = head.val 
            while FILO and val > FILO[-1][0]:
                (_, position) = FILO.pop()
                ans[position] = val
            FILO.append((val, i))
            head = head.next
            ans.append(0)
            i += 1
            
        return ans
            
        
        
        
