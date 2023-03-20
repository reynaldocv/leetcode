# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def helper(word):
            ans = (0, )*26
        
            for char in word: 
                idx = index[char]

                ans = ans[: idx] + (ans[idx] + 1,) + ans[idx + 1: ]

            return ans
            
        n = len(s1)
        
        index = {chr(ord("a") + i): i for i in range(26)}
        
        counter = helper(s1)
                    
        count = helper(s2[: n - 1])
        
        for (i, char) in enumerate(s2[n - 1: ]):
            idx = index[char]
            
            count = count[: idx] + (count[idx] + 1,) + count[idx + 1: ]
            
            if count == counter: 
                return True 
            
            idx = index[s2[i]]
            
            count = count[: idx] + (count[idx] - 1,) + count[idx + 1: ]
            
        return False 
            
               
        
