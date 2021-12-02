# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = {}
        aux = ""
        for i in s: 
            counter[i] = counter.get(i, 0) + 1
            aux = i
        n = counter[aux]
        ans = True
        print(counter)
        for i in s: 
            if counter[i] != n: 
                return False
        return ans
                
            
            
        
