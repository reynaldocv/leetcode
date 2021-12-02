# https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic, dic2 = {}, {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        for num in dic: 
            dic2[dic[num]] = dic2.get(dic[num], [])
            dic2[dic[num]].append(num)
        
        aux, aux2, ans = [], [], []
        for i in dic2:
            aux.append(i)
        aux.sort()
        
        for i in aux: 
            aux2 = []
            for j in dic2[i]:
                aux2.append(j)
            aux2.sort(reverse = True)
            for j in aux2: 
                ans.extend([j]*i)
        
        return ans
