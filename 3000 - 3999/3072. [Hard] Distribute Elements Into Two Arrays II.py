# https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, sort1 = [nums[0]], [nums[0]]
        arr2, sort2 = [nums[1]], [nums[1]]
        
        for num in nums[2: ]: 
            m, n = len(arr1), len(arr2)
            
            idx1 = bisect_left(sort1, num + 1)
            idx2 = bisect_left(sort2, num + 1)
            
            cnt1 = m - idx1
            cnt2 = n - idx2
            
            if cnt1 > cnt2:
                arr1.append(num)
                sort1.insert(idx1, num)
                
            elif cnt2 > cnt1:
                arr2.append(num)
                sort2.insert(idx2, num)
                
            elif m <= n:
                arr1.append(num)
                sort1.insert(idx1, num)                
                
            else: 
                arr2.append(num)                
                sort2.insert(idx2, num)                               
           
        return arr1 + arr2
