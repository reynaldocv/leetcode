# https://leetcode.com/problems/odd-even-jump/

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        large = [-1 for _ in range(n)]
        small = [-1 for _ in range(n)]
        
        aux = [(i, num) for (i, num) in enumerate(arr)]
        
        stack = []
        aux.sort(key=lambda x: (x[1], x[0]))
        
        for (i, num) in aux: 
            while stack and stack[-1] < i: 
                large[stack.pop()] = i
            
            stack.append(i)
        
        stack = []
        aux.sort(key=lambda x: (-x[1], x[0]))        
        
        for (i, num) in aux: 
            while stack and stack[-1] < i: 
                small[stack.pop()] = i
                
            stack.append(i)
        
        odd = [0 for _ in range(n)]
        even = [0 for _ in range(n)]
        odd[-1] = even[-1] = 1
        
        for i in range(n - 1, -1, -1): 
            if large[i] >= 0: 
                odd[i] = even[large[i]]
                
            if small[i] >= 0: 
                even[i] = odd[small[i]]
        
        return sum(odd)
        
