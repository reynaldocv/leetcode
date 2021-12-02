# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}
        repeated = {}
        for i in arr:
            counter[i] = counter.get(i, 0) + 1
        for j in counter:
            if counter[j] not in repeated:
                repeated[counter[j]] = True
            else:
                return False
        return True
            
        
