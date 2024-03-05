# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.counter1 = defaultdict(lambda: 0)
        self.counter2 = defaultdict(lambda: 0)
        
        for num in nums1: 
            self.counter1[num] += 1 
        
        self.nums2 = []
        
        for num in nums2: 
            self.nums2.append(num)
            
            self.counter2[num] += 1 

    def add(self, index: int, val: int) -> None:
        prev = self.nums2[index]
        new = prev + val 
        
        self.nums2[index] = new
        
        self.counter2[prev] -= 1 
        
        if self.counter2[prev] == 0: 
            self.counter2.pop(prev)
            
        self.counter2[new] += 1 
        
    def count(self, tot: int) -> int:
        ans = 0 
        
        for key in self.counter1: 
            tmp = tot - key
            
            if tmp in self.counter2: 
                ans += self.counter1[key]*self.counter2[tmp]
                
        return ans
                
# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
