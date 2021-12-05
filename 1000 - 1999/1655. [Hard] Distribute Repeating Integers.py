# https://leetcode.com/problems/distribute-repeating-integers/

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        def backtracking(i):
            if i == n: 
                return True
            else: 
                for num in counter: 
                    if counter[num] >= 1: 
                        if counter[num] >= quantity[i]:
                            counter[num] -= quantity[i]
                            if backtracking(i + 1):
                                return True
                            counter[num] += quantity[i]
                return False
        
        counter = defaultdict(lambda: 0)
        for num in nums: 
            counter[num] += 1
            
        n = len(quantity)
        quantity.sort(reverse = True)
        
        return backtracking(0)        
        
                
