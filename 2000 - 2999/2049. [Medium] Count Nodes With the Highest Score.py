# https://leetcode.com/problems/count-nodes-with-the-highest-score/

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        def counter(root):            
            if root:                 
                root.left = TreeNode(seen[root.val][0]) if len(seen[root.val]) > 0 else None
                root.right = TreeNode(seen[root.val][1]) if len(seen[root.val]) > 1 else None
                left = counter(root.left)
                right = counter(root.right)
                
                val3 = n - left - right - 1
                
                val1 = 1 if left == 0 else left
                val2 = 1 if right == 0 else right
                val3 = 1 if val3 == 0 else val3
                
                maxProducts[val1*val2*val3] += 1
                
                return 1 + left + right 
            else: 
                return 0 
                
        n = len(parents)
        seen = defaultdict(lambda: [])
        for (i, parent) in enumerate(parents):
            if parent != -1: 
                seen[parent].append(i)
                
        root = TreeNode(0)
        
        maxProducts = defaultdict(lambda: 0)    
        
        counter(root)
        
        return maxProducts[max(maxProducts)]
            
        
