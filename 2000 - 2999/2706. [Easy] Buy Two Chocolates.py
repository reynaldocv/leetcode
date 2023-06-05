# https://leetcode.com/problems/buy-two-chocolates/

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        arr = []
        
        for price in prices: 
            insort(arr, price)
            
            arr = arr[: 2]
        
        if sum(arr) <= money: 
            return money - sum(arr)
        
        else: 
            return money
        
