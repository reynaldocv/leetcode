# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        counter = defaultdict(lambda: 0)
        
        n = len(colors)
        for i in range(1, n - 1):
            if colors[i - 1] == colors[i] and colors[i] == colors[i + 1]:
                counter[colors[i]*3] += 1
                
        return counter["AAA"] > counter["BBB"]
        
