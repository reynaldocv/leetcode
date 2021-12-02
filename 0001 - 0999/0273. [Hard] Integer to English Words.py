# https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        def helper(num):
            if num == 0: 
                return []
            d3 = num // 100
            d2 = (num % 100) // 10
            d1 = num % 10 
            
            ans = []
            if d3 != 0: 
                ans.append(u[d3])
                ans.append("Hundred")
                
            if d2 == 1: 
                ans.append(k[num % 100])
            
            else: 
                if d2 != 0: 
                    ans.append(d[d2])
                if d1 != 0: 
                    ans.append(u[d1])
                    
            return ans
        
        if num == 0: 
            return "Zero"
            
        u = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        d = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
        k = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        
        t = {1: "Thousand", 2: "Million", 3: "Billion"}
        
        totalDig = len(str(num))
        totalDig -= 3 if totalDig % 3 == 0 else totalDig % 3
        totalDig //= 3
        
        ans = []
        while num != 0:
            aux = num // 10**(totalDig*3)
            if aux != 0:
                ans.extend(helper(aux))
            if totalDig != 0 and aux != 0: 
                ans.append(t[totalDig])
            
            num %= 10**(totalDig*3)
            totalDig -= 1
            
        return " ".join(ans)
            
           
