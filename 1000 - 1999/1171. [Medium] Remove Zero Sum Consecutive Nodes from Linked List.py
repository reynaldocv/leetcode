# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode(0, head)
        
        seen = {0: fake}        
        prev = 0
        
        while head:
            prev += head.val            
            seen[prev] = head
            
            head = head.next
            
        head = fake
        prev = 0
        
        while head:
            prev += head.val
            head.next = seen[prev].next
            
            head = head.next
            
        return fake.next

class Solution2:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head: 
            arr.append(head)
            head = head.next
            
        while True: 
            seen = {0: -1}
            n = len(arr)
            prev = 0
            cut = (-1, -1)
            for i in range(n):
                prev += arr[i].val 
                if prev in seen: 
                    cut = (seen[prev] + 1, i + 1)
                    break
                seen[prev] = i
                
            if cut[0] == -1: 
                break
            else: 
                arr = arr[:cut[0]] + arr[cut[1]:]
            
        if arr: 
            for i in range(len(arr) - 1):
                arr[i].next = arr[i + 1]
            arr[~0].next = None

            return arr[0]
        else: 
            return None
