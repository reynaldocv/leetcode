# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        def helper(idx):
            while idx != parent[idx]:
                idx = parent[idx]
                
            return idx 
        
        def collaborator(a, b):
            parentA, parentB = helper(a), helper(b)
            parent[parentA] = parent[parentB] = min(parentA, parentB)
            
        n = len(source)
        parent = [i for i in range(n)]
        
        for (a, b) in allowedSwaps: 
            collaborator(a, b)
        
        elems1 = defaultdict(lambda: defaultdict(lambda: 0))
        elems2 = defaultdict(lambda: defaultdict(lambda: 0))
        for i in range(n):
            parentI = helper(i)
            elems1[parentI][source[i]] += 1 
            elems2[parentI][target[i]] += 1 
            
        ans = 0 
        for key in elems1: 
            for elem in elems1[key]: 
                ans += min(elems1[key][elem], elems2[key][elem])
                
        return n - ans
                
            
        
