# https://leetcode.com/problems/process-restricted-friend-requests/

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:        
        def findParent(i):
            ans = parent[i] 
            while ans != parent[p]: 
                ans = parent[p]
            return ans
        
        parent = [i for i in range(n)]
        
        ans = []
        for (l, r) in requests:
            lParent, rParent = findParent(l), findParent(r) 
            
            parent[lParent] = parent[rParent] = min(lParent, rParent)
            
            blocked = False
            for rl, rr in restrictions:
                pl, pr = findParent(rl), findParent(rr)
                
                if pl == pr:
                    blocked = True
                    parent[lParent], parent[rParent] = lParent, rParent
                    break
                    
            ans.append(not blocked)
        
        return ans
        
