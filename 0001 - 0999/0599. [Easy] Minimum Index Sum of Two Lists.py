# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic, dic2 = {}, {}
        min_  = inf
        for i in range(len(list1)): 
            dic[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in dic: 
                dic2[list2[i]] = i
                min_ = min(min_, dic[list2[i]] + dic2[list2[i]])
        ans = []
        for k in dic2:
            if dic[k] + dic2[k] == min_:
                ans.append(k)
        return ans
            
        
        
        
