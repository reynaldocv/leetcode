# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        index = defaultdict(lambda: [])
        
        for (i, num) in enumerate(nums): 
            index[num].append(i)
            
        ans = 0 
        
        for key in index:
            
            m = len(index[key])
            for i in range(1, m):
                for j in range(i):
                    if index[key][i]*index[key][j] % k == 0: 
                        ans += 1 
            
        return ans
