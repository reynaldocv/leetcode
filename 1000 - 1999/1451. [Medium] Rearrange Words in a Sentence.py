# https://leetcode.com/problems/rearrange-words-in-a-sentence/

class Solution:
    def arrangeWords(self, text: str) -> str:
        arr = [word.lower() for word in text.split(" ")]
        
        arr.sort(key = lambda item: len(item))
        
        arr[0] = arr[0].capitalize() 
        
        return " ".join(arr)
        
