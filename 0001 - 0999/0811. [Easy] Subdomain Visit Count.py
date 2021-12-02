# https://leetcode.com/problems/subdomain-visit-count/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for domain in cpdomains: 
            dom = domain.split(" ")
            web = dom[1].split(".")
            for i in range (len(web)):
                aux = ".".join(web[i:])
                dic[aux] = dic.get(aux, 0) + int(dom[0])
        
        ans = []
        for k in dic: 
            ans.append(str(dic[k]) + " " + k)
        
        return ans
                
        
