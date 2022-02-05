# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        left = defaultdict(lambda: [])
        middle = defaultdict(lambda: [])
        right = defaultdict(lambda: [])
        
        for (a, b, c) in triplets: 
            left[a].append((a, b, c))
            middle[b].append((a, b, c))
            right[c].append((a, b, c))
            
        (l, m, r) = target
        
        for (_, b, c) in left[l]:
            if b <= m and c <= r: 
                for (a, _, c) in middle[m]:
                    if a <= l and c <= r: 
                        for (a, b, _) in right[r]:
                            if a <= l and b <= m: 
                                return True 
                            
        return False
    
    
