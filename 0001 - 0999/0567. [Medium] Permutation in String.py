# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        
        index = {chr(ord("a") + i): i for i in range(26)}
        counter = (0, )*26
        
        for char in s1: 
            idx = index[char]
            
            counter = counter[: idx] + (counter[idx] + 1, ) + counter[idx + 1: ]
            
        counting = (0, )* 26
        
        for char in s2[: m - 1]:
            idx = index[char]
            
            counting = counting[: idx] + (counting[idx] + 1, ) + counting[idx + 1: ]
            
        for (i, char) in enumerate(s2[m - 1: ]):
            idx = index[char]
            
            counting = counting[: idx] + (counting[idx] + 1, ) + counting[idx + 1: ]
            
            if counter == counting: 
                return True 
            
            idx = index[s2[i]]
            
            counting = counting[: idx] + (counting[idx] - 1, ) + counting[idx + 1: ]
            
        return False      
        
