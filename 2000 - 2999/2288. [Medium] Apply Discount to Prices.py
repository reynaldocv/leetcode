# https://leetcode.com/problems/apply-discount-to-prices/

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        def helper(string):
            if string[0] == "$":
                try: 
                    value = float(string[1:])
                    tmp = str(round(value*(100 - discount)/100, 2))
                    n = len(tmp)
                    if tmp.index(".") == n - 2: 
                        tmp += "0"
                        
                    return "$" + tmp
                    
                except: 
                    return string
            else: 
                return string
        
        arr = sentence.split(" ")
        
        n = len(arr)
        
        for i in range(n):
            arr[i] = helper(arr[i])
            
        return " ".join(arr)
