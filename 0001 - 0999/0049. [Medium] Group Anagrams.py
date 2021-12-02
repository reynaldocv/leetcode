# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        dic, ans = {}, []
        for elem in strs: 
            aux = [e for e in elem]
            aux.sort()
            key = "".join(aux)
            dic[key] = dic.get(key, [])
            dic[key].append(elem)
            
        for key in dic: 
            ans.append(dic[key])
        
        return ans
        
            
        
