# https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        ans = []
        if n % 2 == 1: 
            return []
        
        counter = {}
        for num in changed: 
            counter[num] = counter.get(num, 0) + 1
            
        changed.sort()
        
        for num in changed: 
            if counter.get(num, 0) > 0:
                if 2*num in counter and counter[2*num] > 0:
                    counter[num] -= 1
                    counter[2*num] -= 1
                    ans.append(num)
                else: 
                    return []
        
        return ans
                    
