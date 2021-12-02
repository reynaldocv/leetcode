# https://leetcode.com/problems/design-linked-list/

class MyLinkedList:

    def __init__(self):
        self.arr = []        

    def get(self, index: int) -> int:
        if index < len(self.arr):
            return self.arr[index]
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.arr.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.arr.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= len(self.arr):
            self.arr.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.arr):
            del self.arr[index]


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
