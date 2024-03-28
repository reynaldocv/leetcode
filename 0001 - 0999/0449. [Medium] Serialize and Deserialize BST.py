# https://leetcode.com/problems/serialize-and-deserialize-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def helper(node):
            if node: 
                arr.append(str(node.val))
                
                helper(node.left)
                helper(node.right)
                
            else: 
                arr.append("$")
                
        arr = []
        
        helper(root)
        
        return "-".join(arr)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def helper():
            nonlocal idx 
            
            idx += 1 
            
            if arr[idx] != "$":           
                ans = TreeNode(arr[idx])
                
                ans.left = helper()
                ans.right = helper() 
                
                return ans 
            
            else: 
                return None 
            
        arr = data.split("-")
        
        idx = -1
        
        return helper()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
