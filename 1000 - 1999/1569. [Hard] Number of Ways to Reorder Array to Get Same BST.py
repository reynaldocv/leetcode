# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def collaborator(node, val):
            if node: 
                if val < node.val: 
                    node.left = collaborator(node.left, val)
                    
                else: 
                    node.right = collaborator(node.right, val)
                    
                return node
                
            else: 
                return TreeNode(val)
        
        root = None 
        
        def helper(node):
            if node:                 
                (left, qntLeft) = helper(node.left)
                (right, qntRight) = helper(node.right)
                
                total = left*right*supporter(qntLeft + qntRight, qntLeft) 
                total %= MOD
                
                return (total, qntLeft + qntRight + 1)
                
            else: 
                return (1, 0)
 
        def supporter(a, b):
            ans = 1 
            
            for num in range(max(a - b, b) + 1, a + 1):
                ans *= num 
                
            for num in range(2, min(a - b, b) + 1):
                ans //= num 
                
            return ans % MOD
        
        MOD = 10**9 + 7
        
        for num in nums: 
            root = collaborator(root,  num)
            
        return (helper(root)[0] - 1) % MOD
