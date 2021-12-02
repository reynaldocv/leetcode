# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if difference == 0: 
            counter = {num: arr.count(num) for num in arr}
            return max([*counter.values()])
        else:
            if difference < 0: 
                arr = arr[::-1]
                difference *= -1
            counter = {}
            for num in arr: 
                counter[num] = counter.get(num - difference, 0) + 1
            
            return max([*counter.values()])
                    
            
        
