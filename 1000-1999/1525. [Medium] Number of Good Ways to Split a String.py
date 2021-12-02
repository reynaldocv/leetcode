# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        left, right = [], []
        
        counter = defaultdict(lambda: 0)
        for char in s: 
            counter[char] += 1
            left.append(len(counter))
        
        counter = defaultdict(lambda: 0)            
        for char in s[::-1]:
            counter[char] += 1
            right.append(len(counter))
            
        right = right[::-1]
        
        ans = 0
        for i in range(n - 1):
            if left[i] == right[i + 1]:
                ans += 1
            
        return ans
            
