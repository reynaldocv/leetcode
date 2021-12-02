# https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse = True)
        self.arr = nums[:self.k]        

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort(reverse = True)
        self.arr = self.arr[:self.k]
        return self.arr[len(self.arr) - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
