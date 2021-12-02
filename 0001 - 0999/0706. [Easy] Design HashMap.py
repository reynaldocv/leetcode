# https://leetcode.com/problems/design-hashmap/

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        for i in range(len(self.array)):
            if self.array[i][0] == key:
                del self.array[i]                
                break
        self.array.append((key, value))
   
        
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        ans = -1
        for (x, y) in self.array:
            if x == key:
                ans = y
                break
        return ans 
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        ans = -1
        for i in range(len(self.array)):
            if self.array[i][0] == key:
                ans = i
                break
        if ans != -1:
            del self.array[ans]
   
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
