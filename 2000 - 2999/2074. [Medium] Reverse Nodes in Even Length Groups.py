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
            
        start, end, n = 0, 0, len(arr)
        
        k = 2
        while start < n: 
            if (end - start + 1) % 2 == 0: 
                arr[start: end + 1] = arr[start: end + 1][::-1]
            start = end + 1
            end = min(n - 1, end + k)
            k += 1
            
        for i in range(1, n):
            arr[i - 1].next = arr[i]
            
        arr[-1].next = None
            
        return arr[0]
            
        
