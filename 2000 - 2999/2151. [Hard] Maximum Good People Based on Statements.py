# https://leetcode.com/problems/maximum-good-people-based-on-statements/

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int: 
        @cache
        def helper(man):
            good, bad = set([man]), set()
            stack = [man]
            while stack: 
                u = stack.pop()
                for i in range(n):
                    if statements[u][i] == 1: 
                        if i not in good: 
                            good.add(i)
                            stack.append(i)
                    elif statements[u][i] == 0:
                        bad.add(i)
                        
            return good, bad
            
        n = len(statements)
            
        for m in range(n, 0 , -1):
            for comb in combinations(range(n), m):
                allGoods, allBads = set(), set()
                for i in comb: 
                    good, bad = helper(i)
                    allGoods = allGoods.union(good)
                    allBads = allBads.union(bad)
                
                go = True                
                for key in allGoods: 
                    if key in allBads: 
                        go = False
                        break                    
                if go: 
                    return len(comb)
                
        return 0 
