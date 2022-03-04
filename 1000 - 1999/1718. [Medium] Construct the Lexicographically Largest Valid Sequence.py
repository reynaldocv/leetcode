# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

class Solution:    
    def constructDistancedSequence(self, n: int) -> List[int]:
        def helper(cnt, idx):            
            if cnt == 2*n - 1: 
                return True 
            elif ans[idx] == 0:
                for num in range(n, 0, -1):
                    if num not in seen: 
                        idx2 = idx + num if num > 1 else idx
                        if idx2 < 2*n - 1 and ans[idx] == 0 and ans[idx2] == 0: 
                            seen[num] = True 
                            ans[idx] = ans[idx2] = num
                            
                            if helper(cnt + 1, idx + 1):
                                return True 
                            
                            ans[idx] = ans[idx2] = 0
                            seen.pop(num)
            
                return False 
            else: 
                return helper(cnt + 1, idx + 1)
                
                
        seen = {}
        ans = [0 for _ in range(2*n - 1)]
        
        helper(0, 0)
        
        return ans
