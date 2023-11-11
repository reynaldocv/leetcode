# https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def helper(root):
            if not root: 
                return None
            else: 
                root.left = helper(root.left)
                root.right = helper(root.right)
                if root.val in to_delete:
                    if root.left: 
                        ans.append(root.left)
                    if root.right: 
                        ans.append(root.right)
                    return None
                return root
        
        ans = []
        helper(root)
        
        if root.val not in to_delete: 
            ans.append(root)
        
        return ans
        
class Solution2:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def dfs(root, father, izq):
            if root: 
                parent[root.val] = (root, father, izq)
                dfs(root.left, root, 1)
                dfs(root.right, root, 0)
            
        parent = {}
        dfs(root, None, None)
        ans = [root]
        idx = [root.val]
        
        for n in to_delete:
            (node, father, izq) = parent[n]
            if node.left: 
                ans.append(node.left)
                idx.append(node.left.val)
            if node.right: 
                ans.append(node.right)
                idx.append(node.right.val)
            if father: 
                if izq: 
                    father.left = None
                else: 
                    father.right = None 
            if node.val in idx: 
                i = idx.index(node.val)
                del idx[i]
                del ans[i]
        return ans

class Solution3:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def helper(node, parent, left, toAdd): 
            if node: 
                if node.val in toRemove: 
                    if parent:
                        if left: 
                            parent.left = None 
                        
                        else: 
                            parent.right = None 
                        
                    helper(node.left, node, True , True)
                    helper(node.right, node, False, True)
                    
                else: 
                    if toAdd: 
                        ans.append(node)
                        
                    helper(node.left, node, True, False)
                    helper(node.right, node, False, False)
                    
        toRemove = {elem for elem in to_delete}
        
        nodes = {}
        
        ans = []
        
        helper(root, None, True, True)
        
        return ans 
