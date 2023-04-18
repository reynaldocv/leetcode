# https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def helper(node):            
            if node: 
                helper(node.left)
                
                self.arr.append(node.val)
                
                helper(node.right)
            
        self.arr = []
        
        helper(root)
        
        self.idx = 0        

    def next(self) -> int:
        self.idx += 1 
        
        return self.arr[self.idx - 1]
    

    def hasNext(self) -> bool:
        return self.idx < len(self.arr)
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
