# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        
        prev = None 
        
        idx = 0 
        
        while head: 
            if prev != None and head.next != None: 
                if prev < head.val and head.next.val < head.val or prev > head.val and head.next.val > head.val: 
                    arr.append(idx)
                    
            prev = head.val 
            
            head = head.next
            idx += 1 
        
        n = len(arr)
        
        if n <= 1: 
            return [-1, -1]
        
        else: 
            minDiff = inf 
            
            for i in range(n - 1):
                minDiff = min(minDiff, arr[i + 1] - arr[i])
                
            return [minDiff, arr[-1] - arr[0]]
