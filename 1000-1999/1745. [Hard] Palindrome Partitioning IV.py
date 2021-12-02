# https://leetcode.com/problems/palindrome-partitioning-iv/

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def helper(start, m):
            if m == 2:             
                return True if (s[start:] == s[start:][::-1]) else False
            else:
                counter = defaultdict(lambda: 0)
                for i in range(start, n - 1):
                    char = s[i]
                    counter[char] += 1
                    if counter[char] == 2: 
                        del(counter[char])

                    if len(counter) <= 1: 
                        if (s[start: i + 1] == s[start: i + 1][::-1]) and helper(i + 1, m + 1): 
                            return True
        
        n = len(s)
        return helper(0, 0)
                

                
            
