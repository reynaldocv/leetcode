# https://leetcode.com/problems/reconstruct-itinerary/

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def helper(u):
            while graph[u]:
                helper(graph[u].pop())
            ans.insert(0, u)
            
        graph = defaultdict(lambda: [])
        ans = []
        
        for (u, v) in tickets: 
            graph[u].append(v)
            
        for u in graph: 
            graph[u].sort(reverse = True)
            
        helper("JFK")
        
        return ans
        
    
  
