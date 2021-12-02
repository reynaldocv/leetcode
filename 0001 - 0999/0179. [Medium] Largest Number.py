# https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = [str(nums[i]) for i in range(n)]
        
        for i in range(n):
            ans = ("".join(nums[:i + 1]), i)  
            for j in range(i - 1, -1, -1):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                ans = max(ans, ("".join(nums[:i + 1]), j))
                
            elem = nums.pop(0)
            nums.insert(ans[1], elem)            
        
        ans = "".join(nums)        
        return "0" if ans[0] == "0" else ans
        
class Solution2:
    def largestNumber(self, nums: List[int]) -> str:        
        class compare(str):
            def __lt__(x, y):
                return x + y > y + x
    
        n = len(nums)
        nums = [str(nums[i]) for i in range(n)]
        
        largest_num = ''.join(sorted(nums, key = compare))
        
        return '0' if largest_num[0] == '0' else largest_num
