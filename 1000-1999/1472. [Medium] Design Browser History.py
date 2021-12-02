# https://leetcode.com/problems/design-browser-history/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.links = [homepage]
        self.idx = 0
        

    def visit(self, url: str) -> None:
        self.links = self.links[:self.idx + 1]
        self.links.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        if self.idx > steps: 
            self.idx -= steps
        else: 
            self.idx = 0
            
        return self.links[self.idx]    
         
    def forward(self, steps: int) -> str:
        if self.idx < len(self.links) - steps:
            self.idx += steps
        else: 
            self.idx = len(self.links) - 1
             
        return self.links[self.idx]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
