# https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            while x != parent[x]:
                x = parent[x]
            
            return x 
        
        def union(x, y):
            px, py = find(x), find(y)
            parent[px] = parent[py] = min(px, py)
        
        n = len(accounts)
        parent = [i for i in range(n)]
        
        seen = defaultdict(lambda: [])
        
        for (i, account) in enumerate(accounts): 
            for email in account[1:]:
                if email in seen: 
                    union(i, seen[email][0])
                seen[email].append(i)
        
        emails = defaultdict(lambda: set())
            
        for i in range(n):
            idx = find(i)
            for email in accounts[i][1:]:
                emails[idx].add(email)
        
        ans = []
        for idx in emails: 
            aux = [accounts[idx][0]] + sorted(emails[idx])
            ans.append(aux)
            
        return ans
            
