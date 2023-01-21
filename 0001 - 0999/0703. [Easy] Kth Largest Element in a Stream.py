# https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = sorted(nums)
        self.kth = k 

    def add(self, val: int) -> int:
        insort(self.arr, val)
        
        return self.arr[-self.kth]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
