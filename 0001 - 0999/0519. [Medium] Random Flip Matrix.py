# https://leetcode.com/problems/random-flip-matrix/

class Solution:

    def __init__(self, m: int, n: int):
        self.len = m*n
        self.n = n
        self.seen = {}
        
    def flip(self) -> List[int]:        
        rand = randint(0, self.len - 1)
        
        while rand in self.seen: 
            rand += 1
            if rand == self.len:
                rand = 0

        self.seen[rand] = True
        return (rand // self.n, rand % self.n)

    def reset(self) -> None:
        self.seen = {}
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
