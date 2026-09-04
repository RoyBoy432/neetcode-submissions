def traverseThis(stackloc, distance: int):
    x = 0; 
    while x < distance:
        stackloc = stackloc.next; x += 1
    return stackloc

class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None

class MyStack:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def push(self, x: int) -> None:
        if self.size == 0:
            self.head.val = x
            self.size += 1
        else:
            curr = traverseThis(self.head, self.size-1)
            addedNode = ListNode(x)
            curr.next = addedNode
            addedNode.prev = curr
            self.size += 1


    def pop(self) -> int:
        if self.size == 0:
            return None
        else:
            curr = traverseThis(self.head, self.size-1)
            if curr.prev:
                curr.prev.next = None
                self.size -= 1
                return curr.val        
            else:
                temp = curr.val
                curr.val = None
                self.size -= 1
                return temp

            
    def top(self) -> int:
        if self.size == 0:
            return None
        else:
            curr = traverseThis(self.head, self.size-1)
            return curr.val

    def empty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()