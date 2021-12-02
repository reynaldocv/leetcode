# https://leetcode.com/problems/complete-binary-tree-inserter/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        def totalNodes(root):
            cur = root
            hl = 0
            while cur: 
                cur, hl = cur.left, hl + 1
            cur = root
            hr = 0
            while cur: 
                cur, hr = cur.right, hr + 1
            
            if hl == hr: 
                return 2**hl - 1
            else: 
                return 1 + totalNodes(root.left) + totalNodes(root.right)
        
        self.n = totalNodes(root)   
      

    def insert(self, val: int) -> int:
        def insertNode(root, way, value):
            if len(way) == 1:
                if way == "0":
                    root.left = TreeNode(value)                    
                else: 
                    root.right = TreeNode(value)
                return root.val
            elif way[0] == "0": 
                return insertNode(root.left, way[1:], value)
            else:
                return insertNode(root.right, way[1:], value)
        
        way = str(bin(self.n + 1))[3:]        
        self.n += 1        
        return insertNode(self.root, way, val)
    
    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
