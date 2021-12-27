# https://leetcode.com/problems/rank-teams-by-votes/

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        count = defaultdict(lambda: (0, )*n)
        
        for vote in votes: 
            for (i, char) in enumerate(vote):
                count[char] = count[char][: i] + (count[char][i] - 1,) + count[char][i + 1:] 
                
        ans = [key for key in count]
        
        ans.sort(key = lambda item: (count[item], item))
        
        return "".join(ans)
