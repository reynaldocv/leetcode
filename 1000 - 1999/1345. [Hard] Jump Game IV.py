# https://leetcode.com/problems/jump-game-iv/

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1: 
            return 0 
        
        index = defaultdict(lambda: [])
        for (i, num) in enumerate(arr):
            index[num].append(i)
                
        stack1 = set([0])        
        stack2 = set([n - 1])
        
        ans = 0
        seen = {0: True, n - 1: True}
        
        while stack1: 
            if len(stack1) > len(stack2):
                stack1, stack2 = stack2, stack1
                
            newStack = set([])
            
            for u in stack1:                 
                for v in [u - 1, u + 1]:                    
                    if v in stack2: 
                        return ans + 1
                    if 0 <= v < n and v not in seen:
                        seen[v] = True
                        newStack.add(v)
                
                for idx in index[arr[u]]:
                    if idx in stack2: 
                        return ans + 1
                    if idx not in seen: 
                        seen[idx] = True
                        newStack.add(idx)
                        
                index.pop(arr[u])
                        
            stack1 = newStack
            ans += 1 
        
        return -1
            
                
                
                
            
        
