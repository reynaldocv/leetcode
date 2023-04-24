# https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        counter = defaultdict(lambda: defaultdict(lambda: 0))
        
        for (type, color, name) in items: 
            counter["type"][type] += 1
            counter["color"][color] += 1 
            counter["name"][name] += 1 
            
        return counter[ruleKey][ruleValue]
            
        
            
            
        
    
        
