# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        
        while head: 
            arr.append(head)
            
            head = head.next 
            
        n = len(arr)
        
        if n == 1: 
            return arr[0]
        
        for i in range(n - 1):
            node = ListNode(gcd(arr[i].val, arr[i + 1].val))
            
            arr[i].next = node
            node.next = arr[i + 1]
            
        return arr[0]
            
