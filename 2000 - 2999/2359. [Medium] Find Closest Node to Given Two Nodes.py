# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        seen1 = defaultdict(lambda: inf)
        seen1[node1] = 0 
        stack = [(node1, 0)]
        
        while stack: 
            (u, dist) = stack.pop() 
            v = edges[u]
            
            if v != -1 and v not in seen1: 
                seen1[v] = dist + 1
                stack.append((v, dist + 1))
                
        seen2 = defaultdict(lambda: inf)
        seen2[node2] = 0 
        stack = [(node2, 0)]
                
        while stack: 
            (u, dist) = stack.pop() 
            v = edges[u]
            
            if v != -1 and v not in seen2: 
                seen2[v] = dist + 1
                stack.append((v, dist + 1))
                
        ans = max((seen1[node2], node2), (seen2[node1], node1))
        
        for key in seen1: 
            if key in seen2: 
                ans = min(ans, max((seen1[key], key), (seen2[key], key)))
                
        return ans[1] if ans[0] != inf else -1
                
