# https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        counter = defaultdict(lambda: 0)
        a, b = pattern[0], pattern[1]
        if a != b:
            ans = 0 
            for char in text: 
                if char == b:
                    ans += counter[a]
                    counter[b] += 1 
                if char == a: 
                    counter[a] += 1 

            return ans + max(counter[a], counter[b])

        else: 
            for char in text: 
                if char == a: 
                    counter[a] += 1 
                    
            return counter[a]*(counter[a] + 1)//2
