# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def helper(u):
            distance = defaultdict(lambda: inf)
            distance[u] = 0 

            stack = [(u, 0)]

            while stack: 
                (u, dist) = stack.pop() 
                v = edges[u]

                if v != -1 and v not in distance: 
                    distance[v] = dist + 1
                    stack.append((v, dist + 1))

            return distance
        
        distance1 = helper(node1)
        
        distance2 = helper(node2)
                
        ans = (inf, -1)
        
        for key in distance1: 
            if key in distance2: 
                tmp = max(distance1[key], distance2[key])
                ans = min(ans, (tmp, key))
                
        return ans[1] 
                
