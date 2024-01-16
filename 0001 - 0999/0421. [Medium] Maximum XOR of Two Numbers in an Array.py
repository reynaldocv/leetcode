# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def helper(num):
            node1 = trie
            
            for i in range(32, -1, -1):
                bit = (num >> i) & 1
                
                if bit not in node: 
                    node[bit] = {}
                    
                node = node[bit]
                
            node["$"] = num
                
        def collaborator(num):
            node = trie
            
            for i in range(32, -1, -1):
                bit = (num >> i) & 1
                
                if 1 - bit in node: 
                    node = node[1 - bit] 
                    
                else: 
                    node = node[bit]
                    
            return node["$"]
        
        trie = {}
        
        ans = 0 
        
        for num1 in nums: 
            helper(num1)
            
            num2 = collaborator(num1)
            
            ans = max(ans, num1^num2)
            
        return ans 
