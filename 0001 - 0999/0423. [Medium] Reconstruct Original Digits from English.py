# https://leetcode.com/problems/reconstruct-original-digits-from-english/

class Solution:
    def originalDigits(self, s: str) -> str:
        counter = defaultdict(lambda: 0)
        dic1 = OrderedDict()
        dic1["g"] = ("it", 8)   
        dic1["z"] = ("o" , 0)   
        dic1["w"] = ("to", 2)   
        dic1["u"] = ("fo" , 4)   
        dic1["x"] = ("i" , 6)   
        dic1["o"] = ("", 1)   
        dic1["t"] = ("", 3)   
        dic1["f"] = ("iv", 5)   
        dic1["v"] = ("", 7)   
        dic1["i"] = ("", 9)  
        
        for char in s: 
            counter[char] += 1
        
        counter2 = [0 for _ in range(10)]
        
        for key in dic1: 
            quantity = counter[key]
            if quantity > 0: 
                counter2[dic1[key][1]] = quantity
                for char in dic1[key][0]:
                    counter[char] -= quantity

        ans = []
        for i in range(10):
            ans.append(str(i)*counter2[i])
        
        return "".join(ans)
        
        
                
        
