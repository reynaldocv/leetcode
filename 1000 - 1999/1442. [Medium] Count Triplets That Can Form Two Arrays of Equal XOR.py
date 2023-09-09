# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        index = defaultdict(lambda: [])
        
        prev = 0 
        
        index[prev].append(-1)
        
        for (i, num) in enumerate(arr): 
            prev ^= num
            
            index[prev].append(i)
            
        ans = 0 

        for key in index: 
            arr = index[key]
            m = len(arr)
            
            for i in range(m - 1):
                for j in range(i + 1, m):
                    ans += arr[j] - arr[i] - 1
                    
        return ans 
        
        
