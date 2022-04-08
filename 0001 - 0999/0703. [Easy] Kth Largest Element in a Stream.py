# https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.arr = []
        
        for num in nums: 
            insort(self.arr, num)
        
    def add(self, val: int) -> int:
        insort(self.arr, val)
        
        return self.arr[len(self.arr) - self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
