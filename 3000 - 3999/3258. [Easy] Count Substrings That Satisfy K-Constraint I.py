# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        counter = defaultdict(lambda: -1)
        cnt = [0, 0]
        
        index = defaultdict(lambda: defaultdict(lambda: -1))
        
        ans = 0 
        
        for (ith, char) in enumerate(s):
            bit = int(char)
            
            cnt[bit] += 1 
            
            start = min(index[0][cnt[0] - k], index[1][cnt[1] - k])
            
            ans += ith - start
            
            index[bit][cnt[bit]] = ith 
            
        return ans 
            
