# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.counter1 = defaultdict(lambda: 0)
        self.counter2 = defaultdict(lambda: 0)
        self.number = defaultdict(lambda: -1)
        
        for num in nums1: 
            self.counter1[num] += 1
        
        for (i, num) in enumerate(nums2): 
            self.counter2[num] += 1
            self.number[i] = num

    def add(self, index: int, val: int) -> None:
        num = self.number[index]
        
        self.counter2[num] -= 1
        if self.counter2[num] == 0: 
            self.counter2.pop(num)
            
        self.counter2[num + val] += 1
        self. number[index] = num + val

    def count(self, tot: int) -> int:
        ans = 0 
        
        for numA in self.counter1: 
            numB = tot - numA
            if numB in self.counter2: 
                ans += self.counter1[numA]*self.counter2[numB]
                
        return ans
        

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
