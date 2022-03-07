# https://leetcode.com/problems/create-binary-tree-from-descriptions/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        def helper(val):
            tree = TreeNode(val)
            for (son, isLeaft) in graph[val]:
                if isLeaft:
                    tree.left = helper(son)
                else:
                    tree.right = helper(son)
                    
            return tree
        
        
        counter = defaultdict(lambda: 0)
        graph = defaultdict(lambda: [])
        elems = {}
        
        for (parent, son, isLeft) in descriptions: 
            graph[parent].append((son, isLeft))            
            counter[son] += 1
            elems[parent] = elems[son] = True
      
        root = [key for key in elems if counter[key] == 0]
        
        ans = helper(root[0])
        
        return ans
