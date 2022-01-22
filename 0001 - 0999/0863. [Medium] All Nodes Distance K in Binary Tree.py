# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def helper(node, arr):
            nonlocal stack
            if node: 
                if node == target:   
                    arr.append(target)
                    stack = arr[:]
                else: 
                    helper(node.left, arr + [node])
                    helper(node.right, arr + [node])
        
        def collaborator(node, k):
            if node:
                if k == 0: 
                    ans.append(node.val)
                elif k > 0:
                    return collaborator(node.left, k - 1) + collaborator(node.right, k - 1)
                
            return 0 
            
        if k == 0: 
            return [target.val]
        
        ans = [] 
        stack = []
        helper(root, [])
        n = len(stack)
        
        for i in range(n - 1):
            h = k - (n - i - 1)
            if h >= 0: 
                node = stack[i]
                if h == 0: 
                    ans.append(node.val)
                else:
                    if node.left != stack[i + 1]:
                        collaborator(node.left, h - 1)            
                    if node.right != stack[i + 1]:
                        collaborator(node.right, h - 1)

        
        collaborator(stack[-1], k)
        
        return ans
            
            
            
