# https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        index = defaultdict(lambda: [])
        
        for (i, char) in enumerate(s):
            index[char].append(i)
            
        ans = 0 
        for word in words: 
            prev = -inf
            go = True
            for char in word:  
                idx = bisect_left(index[char], prev + 1)
                if idx == len(index[char]):
                    go = False
                    break
                else: 
                    prev = index[char][idx]
            
            ans += 1 if go else 0 
            
        return ans
