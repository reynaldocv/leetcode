# https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.ans = []
        self.idx = -1
        
        def helper(root):
            if root: 
                helper(root.left)
                self.ans.append(root.val)
                helper(root.right)
        
        helper(root)
        
    def next(self) -> int:
        self.idx += 1
        return self.ans[self.idx] if self.idx < len(self.ans) else -4
        
    def hasNext(self) -> bool:
        return True if self.idx < len(self.ans) - 1 else False

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
