# https://leetcode.com/problems/design-browser-history/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.idx = 0 

    def visit(self, url: str) -> None:
        self.pages = self.pages[: self.idx + 1]
        
        self.pages.append(url)
        self.idx += 1 
        
    def back(self, steps: int) -> str:
        if self.idx - steps < 0:
            self.idx = 0 
            
        else:
            self.idx -= steps
            
        return self.pages[self.idx]
    
    def forward(self, steps: int) -> str:
        if self.idx + steps >= len(self.pages):
            self.idx = len(self.pages) - 1
            
        else: 
            self.idx += steps
            
        return self.pages[self.idx]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
        
