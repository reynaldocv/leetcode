# https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = {}
        for num in arr: 
            dic[num] = dic.get(num, 0) + 1
        
        ans = -1
        for k in dic: 
            if k == dic[k]:
                ans = max(ans, k)
                
        return ans
