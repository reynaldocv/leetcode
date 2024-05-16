# https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix:

    def __init__(self, n: int):
        self.arr = [0]
        
        self.end = n         

    def upload(self, video: int) -> None:
        insort(self.arr, video)

    def longest(self) -> int:
        start = 0 
        end = len(self.arr) 
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if self.arr[mid] == mid: 
                start = mid 
                
            else: 
                end = mid 
                
        return start

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
