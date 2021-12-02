# https://leetcode.com/problems/throne-inheritance/

class person():
    def __init__(self, name: str): 
        self.name = name
        self.alive = 1
        self.children = []

class ThroneInheritance:

    def __init__(self, kingName: str):
        king = person(kingName)
        self.king = king
        self.seen = {king.name: king}
        

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.seen: 
            son = person(childName)
            self.seen[parentName].children.append(son)
            self.seen[son.name] = son

    def death(self, name: str) -> None:
        if name in self.seen: 
            self.seen[name].alive = 0 
        

    def getInheritanceOrder(self) -> List[str]:
        def helper(king):
            if king: 
                if king.alive == 1: 
                    ans.append(king.name)
                for child in king.children: 
                    helper(child)
        
        ans = []
        helper(self.king)
        
        return ans
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
