# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        start = 0 
        
        ans = 0 
    
        for (i, fruit) in enumerate(fruits):
            counter[fruit] += 1 
            
            while len(counter) > 2: 
                oldFruit = fruits[start]
                
                counter[oldFruit] -= 1 
        
                if counter[oldFruit] == 0: 
                    counter.pop(oldFruit)
                    
                start += 1 
            
            ans = max(ans, i - start + 1)
            
        return ans 

            
                
                
            
                
            
