# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def counter(s):
            counter = {}
            for char in s: 
                counter[char] = counter.get(char, 0) + 1
                if counter[char] > 1: 
                    return False
            return True
        
        def helper(s, i):
            if i == n:                 
                if counter(s): 
                    self.ans = max(self.ans, len(s))
            else: 
                helper(s, i + 1)
                if counter(s + arr[i]):
                    helper(s + arr[i], i + 1)
        
        n = len(arr)
        self.ans = 0
        helper("", 0)
        
        return self.ans
                    
        
