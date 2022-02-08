# https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers:

    def __init__(self):
        self.lastZero = -1
        self.products = [1]
        self.idx = 0 
    
    def add(self, num: int) -> None:
        if num == 0: 
            self.lastZero = self.idx
            if self.idx == 0: 
                self.products.append(1)
            else: 
                self.products.append(self.products[-1])
        else: 
            if self.idx == 0: 
                self.products.append(num)
            else: 
                self.products.append(self.products[-1]*num)
        
        self.idx += 1 
        
    def getProduct(self, k: int) -> int:
        aux = self.idx - k 
        if aux >= 0 and aux > self.lastZero: 
            return self.products[-1]//self.products[-(k + 1)]
        else: 
            return 0 
        
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
