# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def diff(arr, arr2, arr3):
            aux = arr.copy()
            n = len(arr)
            for i in range(n):
                aux[i] = arr[i] - arr2[i]
            return aux == arr3
            
        idx = {val: i for (i, val) in enumerate(set(sorted(s1)))}
        values = {i: val for (i, val) in enumerate(set(sorted(s1)))}
        
        count = [s1.count(values[i]) for i in range(len(idx))]
        
        n = len(s2)
        m = len(s1)
        counter = {-1: [0 for _ in idx]}
        
        for (i, val) in enumerate(s2):
            counter[i] = counter[i - 1].copy()
            if val in idx: 
                counter[i][idx[val]] += 1
                if i - m in counter: 
                    if diff(counter[i], counter[i - m], count):
                        return True
        
        return False
                    
                
      
        
