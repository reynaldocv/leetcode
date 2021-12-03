# https://leetcode.com/problems/apply-discount-every-n-orders/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n 
        self.nth = 1
        self.discount = discount
        self.prices = {product: prices[i] for (i, product) in enumerate(products)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        def getTotal(product, amount):
            ans = 0 
            for (idx, cnt) in zip(product, amount):
                ans += cnt*self.prices[idx]
            
            return ans
        
        def getDiscount(total):
            if self.nth % self.n == 0: 
                self.nth = 1
                return total*((100- self.discount)/100)
            else: 
                self.nth += 1
                return total 
            
        return getDiscount(getTotal(product, amount))

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
