# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dishes = {}
        order = defaultdict(lambda: defaultdict(lambda: 0))
        
        for (idx, tableIdx, dish) in orders: 
            dishes[dish] = True
            order[tableIdx][dish] += 1
            
        dishes = list(dishes.keys())
        dishes.sort()
        
        ans = [["Table"] + dishes]
                      
        tablesIdx = list(order.keys())
        tablesIdx.sort(key = lambda item: int(item))
        
        for key in tablesIdx: 
            aux = [key]                
            for dish in dishes: 
                aux.append(str(order[key][dish]))
            
            ans.append(aux)
            
        return ans
