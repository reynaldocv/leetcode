# https://leetcode.com/problems/subdomain-visit-count/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(lambda: 0)
        
        for domain in cpdomains: 
            num, domains = domain.split(" ")
            
            urls = domains.split(".")
            
            n = len(urls)
            
            for i in range(n):
                word = ".".join(urls[i: ])
                
                counter[word] += int(num)
                
        return [str(counter[key]) + " " + key for key in counter]
                
        
