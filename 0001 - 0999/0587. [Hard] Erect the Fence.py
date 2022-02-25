# https://leetcode.com/problems/erect-the-fence/

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        (x, y) = min(trees, key = lambda x: (x[1], x[0])) 
        
        points = defaultdict(lambda: [])
        for (r, s) in trees: 
            points[atan2(s - y, r - x)].append((r, s))
        
        trees = []
        keys = sorted(points)
        for key in keys: 
            points[key].sort(key = lambda item: abs(item[0] - x) + abs(item[1] - y))
            if key == keys[-1]: 
                points[key].reverse()
                
            trees.extend(points[key])
                
        stack = []
        
        for (x, y) in trees: 
            while len(stack) >= 2: 
                (x0, y0) = stack[-1]
                (x1, y1) = stack[-2]
                if (x0 - x1)*(y - y0) - (x - x0)*(y0 - y1) >= 0: 
                    break
                else: 
                    stack.pop()
                    
            stack.append((x, y))
            
        return stack
        
