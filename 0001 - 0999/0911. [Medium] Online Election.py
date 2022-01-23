# https://leetcode.com/problems/online-election/

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.winner = []     
        self.times = times
        self.n = len(persons)
        
        winner = (-inf, -inf, "$")
        counter = defaultdict(lambda: 0)
        
        for (i, person) in enumerate(persons): 
            counter[person] += 1            
            winner = max(winner, (counter[person], i, person))
            self.winner.append(winner)
            
    def q(self, t: int) -> int:
        idx = bisect_left(self.times, t)
        if idx == self.n:
            idx -= 1
        elif self.times[idx] > t: 
            idx -= 1
                    
        return self.winner[idx][2]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
