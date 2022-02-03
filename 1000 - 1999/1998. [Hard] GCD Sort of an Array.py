# https://leetcode.com/problems/gcd-sort-of-an-array/

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        def helper(node):
            while node != parent[node]:
                node = parent[node]
                
            return node
        
        def collaborator(node1, node2):
            parent1 = helper(node1)
            parent2 = helper(node2)
            parent[parent1] = parent[parent2] = min(parent1, parent2)
            
        maxElem = max(nums)
        parent = [i for i in range(maxElem + 1)]
        
        seen = {num: True for num in nums}
        
        sieve = [1 for i in range(maxElem + 1)]
        sieve[0] = sieve[1] = 0
        
        for k in range(maxElem//2 + 1):
            if sieve[k]:
                for x in range(2*k, maxElem + 1, k):
                    sieve[x] = 0 
                    if x in seen: 
                        collaborator(k, x)
                        
        arr = sorted(nums)
        
        for (i, num) in enumerate(arr):
            if helper(num) != helper(nums[i]):
                return False
            
        return True 
    
        
        
