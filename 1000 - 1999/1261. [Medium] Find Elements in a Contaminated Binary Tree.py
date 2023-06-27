# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def helper(node, value):
            if node: 
                self.seen.add(value)
                
                helper(node.left, 2*value + 1)
                helper(node.right, 2*value + 2)
        
        self.seen = set()
        
        helper(root, 0)

    def find(self, target: int) -> bool:
        return target in self.seen

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
