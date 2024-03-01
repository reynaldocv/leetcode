# https://leetcode.com/problems/rank-teams-by-votes/

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        
        counter = defaultdict(lambda: (0, )*n)
        
        for vote in votes: 
            for (i, char) in enumerate(vote):
                counter[char] = counter[char][: i] + (counter[char][i] - 1, ) + counter[char][i + 1: ]
                
        arr = [key for key in counter]
        
        arr.sort(key = lambda item: (counter[item], item))
        
        return "".join(arr)
