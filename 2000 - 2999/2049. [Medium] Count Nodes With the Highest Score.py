# https://leetcode.com/problems/count-nodes-with-the-highest-score/

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        @cache        
        def helper(u):
            ans = 1 
            
            for v in graph[u]:
                ans += helper(v)
                
            return ans 
        
        n = len(parents)
        
        graph = defaultdict(lambda: [])
        
        for (i, val) in enumerate(parents):
            graph[val].append(i)
            
        scores = []   
        maxFreq = 0 
        
        for u in range(n):
            score = 1
            nodes = 0 
            
            for v in graph[u]:
                score *= helper(v)
                nodes += helper(v)
                
            remain = n - nodes - 1
            
            if remain > 0: 
                score *= remain
                
            scores.append(score)
            maxFreq = max(maxFreq, scores[u])
            
        ans = 0 
        
        for score in scores: 
            if score == maxFreq: 
                ans += 1 
                
        return ans 
            
            
        
