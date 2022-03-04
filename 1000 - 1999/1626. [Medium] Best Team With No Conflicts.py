# https://leetcode.com/problems/best-team-with-no-conflicts/

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        arr = [(scores[i], ages[i]) for i in range(n)]
        
        arr.sort()
        
        ans = [0 for i in range(n)]
        
        for i in range(n):
            aux = 0 
            for j in range(i):
                if arr[i][1] >= arr[j][1]:
                    aux = max(aux, ans[j])
                
            ans[i] = aux + arr[i][0]
            
        return max(ans)
                
