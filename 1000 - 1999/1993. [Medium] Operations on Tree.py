# https://leetcode.com/problems/operations-on-tree/

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.graph = defaultdict(lambda: [])
        
        for (i, father) in enumerate(parent):
            self.graph[father].append(i)
            
        self.locked = defaultdict(lambda: False)
        
    def lock(self, num: int, user: int) -> bool:
        if num not in self.locked: 
            self.locked[num] = user
            return True 
        
        return False
        
    def unlock(self, num: int, user: int) -> bool:
        if num in self.locked: 
            if self.locked[num] == user: 
                self.locked.pop(num)
                return True 
            
        return False 

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked: 
            return False 
        
        go = True 
        
        node = num 
        
        while node != -1: 
            if node in self.locked: 
                go = False
                break
            
            node = self.parent[node]
            
        if go:  
            stack = [num]
            descendant = []
            while stack: 
                node = stack.pop()
                
                if node in self.locked: 
                    descendant.append(node)
                
                for child in self.graph[node]:
                    stack.append(child)
                    
            if descendant: 
                self.locked[num] = user
                
                for node in descendant: 
                    self.locked.pop(node)
                    
                return True 
        
        return False 

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)


            
