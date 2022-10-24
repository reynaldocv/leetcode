# https://leetcode.com/problems/sort-array-by-parity/

class Solution1:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key = lambda item: item % 2)
        
class Solution2:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans1 = []
        ans2 = [] 
        l = len(A)
        for i in range(l):
            if A[i] % 2 == 0: 
                ans1.append(A[i])
            else:
                ans2.append(A[i])
        return ans1 + ans2
            
            
                
