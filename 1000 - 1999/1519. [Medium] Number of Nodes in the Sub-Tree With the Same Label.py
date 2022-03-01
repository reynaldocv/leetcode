# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def helper(u):            
            counter = defaultdict(lambda: 0)
            if u in seen: 
                return counter
            
            else: 
                seen[u] = True 
                for v in graph[u]:
                    cnt = helper(v)
                    for key in cnt: 
                        counter[key] += cnt[key]

                counter[labels[u]] += 1 
                ans[u] = counter[labels[u]]

                return counter
        
        graph = defaultdict(lambda: [])
        for (a, b) in edges: 
            graph[a].append(b)
            graph[b].append(a)
            
        seen = {}
        
        ans = [0 for _ in range(n)]
            
        helper(0)
        
        return ans 
