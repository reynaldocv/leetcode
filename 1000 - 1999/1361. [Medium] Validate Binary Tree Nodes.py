# https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def helper(u):
            if u != -1: 
                if u in seen: 
                    return False 
                else: 
                    seen[u] = True
                    return helper(leftChild[u]) and helper(rightChild[u])
            else: 
                return True 
        
        counter = defaultdict(lambda: 0)
        for i in range(n):
            if leftChild[i] != -1:
                counter[leftChild[i]] += 1 
            if rightChild[i] != -1:
                counter[rightChild[i]] += 1
            
        roots = [i for i in range(n) if counter[i] == 0]
        
        if len(roots) != 1: 
            return False 
        
        u = roots.pop()
        seen = {}
        
        return helper(u) and len(seen) == n
