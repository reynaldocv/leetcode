# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = []
        node = 1
        lvl = 0 
        
        while label >= node*2:
            node *= 2
            lvl += 1
            
        while lvl >= 0: 
            ans.append(label)
            lvlMin, lvlMax = 2**lvl, 2**(lvl + 1) - 1
            label = (lvlMax + lvlMin - label)//2
            lvl -= 1
            
        return ans[::-1]
            
            
         
