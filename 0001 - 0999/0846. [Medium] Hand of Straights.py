# https://leetcode.com/problems/hand-of-straights/

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = defaultdict(lambda: 0)
        
        for num in hand: 
            counter[num] += 1 
        
        nums = sorted(key for key in counter)
        
        m = len(nums)
        
        for i in range(m - groupSize + 1):
            num = nums[i]            
            
            if num in counter:             
                times = counter[num]
            
                for j in range(groupSize):
                    if num + j == nums[i + j] and nums[i + j] in counter and counter[nums[i + j]] >= times: 
                        counter[num + j] -= times
                        
                        if counter[num + j] == 0: 
                            counter.pop(num + j)
                        
                    else: 
                        return False 
        
        return len(counter) == 0
        
        
        
