# https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        
        seen = {(0, n), (m, n - 1), (m - 1, -1)}
        
        x, y = 0, -1
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        k = 0 
        
        ith = 0 
        
        while head: 
            x += directions[k][0]
            y += directions[k][1]
            
            if (x, y) not in seen:
                ans[x][y] = head.val 
            
                head = head.next
                seen.add((x, y))
                
            else: 
                x -= directions[k][0]
                y -= directions[k][1]
                
                k = (k + 1) % 4
                
        return ans 
            
