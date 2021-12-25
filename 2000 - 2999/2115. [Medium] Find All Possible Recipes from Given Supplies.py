# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(lambda:[])
        req = defaultdict(lambda:[])
        
        for (i, recipe) in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
                
            req[recipe] = len(ingredients[i])
            
        stack = [supply for supply in supplies]
        ans = []
        
        while stack: 
            u = stack.pop()
            for v in graph[u]:
                req[v] -= 1
                if req[v] == 0:
                    stack.append(v)
                    ans.append(v)
                    
        return ans
         
        
                
