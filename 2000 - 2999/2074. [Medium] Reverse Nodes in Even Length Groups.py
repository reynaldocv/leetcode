# https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        
        while head: 
            arr.append(head)
            
            head = head.next
            
        n = len(arr)
        
        start = 0 
        lenght = 1
        
        even = False 
        
        while start < n:   
            end = min(start + lenght, n)
            
            if (end - start) % 2 == 0:
                arr[start: end] = arr[start: end][:: -1]
                
            start = end 
            lenght += 1 
            
            even = not even
            
        for i in range(n - 1):
            arr[i].next = arr[i + 1]
            
        arr[-1].next = None 
        
        return arr[0]
            
        
