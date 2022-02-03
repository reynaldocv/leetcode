# https://leetcode.com/problems/shopping-offers/

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def collaborator(arr1, arr2):
            ans = [0 for _ in range(n)]
            for i in range(n):
                ans[i] = arr1[i] - arr2[i]
                if ans[i] < 0: 
                    return False, []
            
            return True, ans                
        
        def helper(idx, needs):
            if sum(needs) == 0: 
                return 0 
            else: 
                ans = 0 
                for (i, need) in enumerate(needs):
                    ans += need*price[i]
                
                for j in range(idx, m):
                    go, arr = collaborator(needs, special[j][:-1])
                    if go:
                        ans = min(ans, special[j][-1] + helper(j, arr))
                
                return ans 
            
        n = len(price)
        m = len(special)
        
        ans = inf
        
        return helper(0, needs)
        
        
