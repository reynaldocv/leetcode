# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        seen = defaultdict(lambda: defaultdict(lambda: 0))
        
        dishes = set()
        tables = set()
        
        for (_, table, dish) in orders: 
            seen[table][dish] += 1 
            
            dishes.add(dish)
            tables.add(table)
            
        dishes = [dish for dish in dishes]
        tables = [table for table in tables]
        
        dishes.sort() 
        tables.sort(key = lambda item: int(item))
        
        ans = [["Table"]]
        
        for dish in dishes: 
            ans[0].append(dish)
            
        for table in tables: 
            tmp = [str(table)]
            
            for dish in dishes: 
                tmp.append(str(seen[table][dish]))
                
            ans.append(tmp)
            
        return ans 
