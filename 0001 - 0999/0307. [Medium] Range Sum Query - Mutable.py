# https://leetcode.com/problems/range-sum-query-mutable/

class NumArray:

    def __init__(self, nums: List[int]):
        def buildTree(nums):
            for i in range(n):
                tree[i + n] = nums[i]
            
            for i in range(n - 1, 0, -1):
                tree[i] = tree[2*i] + tree[2*i + 1]
                
        self.n = n = len(nums)
        if n > 0: 
            self.tree = tree = [0]*2*n
            buildTree(nums)
        
    def update(self, index: int, val: int) -> None:
        index += self.n
        self.tree[index] = val
        while index > 0: 
            left = index
            right = index
            if index % 2 == 0: 
                right = index + 1
            else: 
                left = index - 1
            
            self.tree[index//2] = self.tree[left] + self.tree[right]
            index //= 2
        
    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        
        ans = 0 
        while left <= right: 
            if left % 2 == 1: 
                ans += self.tree[left]
                left += 1
            if right % 2 == 0: 
                ans += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        
        return ans

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
