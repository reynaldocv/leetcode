# https://leetcode.com/problems/largest-component-size-by-common-factor/

class UnionFind: 
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        
    def find(self, p): 
        while p != self.parent[p]: 
            p = self.parent[p]
        return p
    
    def union(self, p, q): 
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: 
            return False 
        if self.rank[prt] > self.rank[qrt]: 
            prt, qrt = qrt, prt
            
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        
        return True 


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        m = max(A)
        uf = UnionFind(m + 1)
        seen = set(A)
        
        sieve = [1]*(m + 1)
        sieve[0] = sieve[1] = 0 
        for k in range(m//2 + 1): 
            if sieve[k]: 
                ref = k if k in seen else 0
                for x in range(2*k, m + 1, k): 
                    sieve[x] = 0
                    if x in seen: 
                        if ref: 
                            uf.union(ref, x)
                        ref = x
        
        freq = defaultdict(lambda: 0)
        for i in range(m + 1):
            freq[uf.find(i)] += 1
            
        return max(freq.values())
