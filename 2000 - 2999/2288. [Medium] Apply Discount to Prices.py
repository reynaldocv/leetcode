# https://leetcode.com/problems/apply-discount-to-prices/

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(" ")
        
        for (i, word) in enumerate(words): 
            if len(word) > 1 and word[0] == "$" and word[1: ].isdigit(): 
                value = int(word[1: ])*(100 - discount)/100
                
                strVal = str(value)
                
                if "." in strVal: 
                    strVal += "00"
                    
                    m = len(strVal)                    
                    idx = strVal.index(".")
                    
                    strVal = strVal[: idx + 3]
                    
                else: 
                    strVal += ".00"
        
                words[i] = "$" + strVal 
            
        return " ".join(words)
                
