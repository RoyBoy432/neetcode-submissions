def traverseThis(distance: int, lnstart: ListNode):
    x = 0; curr = lnstart
    while x < distance:
        curr = curr.next; x += 1
    return curr


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.length = 0
        

    def get(self, index: int) -> int:
        if index+1 > self.length:
            return -1
        else:
            curr = traverseThis(index, self.head)
            return curr.val
        

    def addAtHead(self, val: int) -> None:
        if self.length == 0:
            self.head.val = val; self.length += 1
        elif self.length > 0:
            addedNode = ListNode(val)
            addedNode.next = self.head
            addedNode.prev = None
            self.head.prev = addedNode
            self.head = addedNode
            self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.head.val = val; self.length += 1
        elif self.length > 0:
            tail = traverseThis(self.length-1,self.head)
            addedNode = ListNode(val)
            addedNode.next = None
            addedNode.prev = tail
            tail.next = addedNode
            self.length += 1
        '''elif self.length > 0:
            tail = self.head
            while tail:
                tail = tail.next
            addedNode = ListNode(val)
            addedNode.next = None
            addedNode.prev = tail
            tail.next = addedNode
            self.length+=1'''


    def addAtIndex(self, index: int, val: int) -> None:
        if self.length == 0 and index == 0:
            self.head.val = val; self.length += 1
        elif index > self.length:
            pass
        else:
            if index == self.length:
                self.addAtTail(val)
            elif index == 0:
                self.addAtHead(val)
            else:
                curr = traverseThis(index, self.head)
                #x = 0; curr = self.head
                #while x < index:            
                #    curr = curr.next; x += 1
                    #now curr is node1
                    #so I need to add the new thing to the left of node1
                addedNode = ListNode(val)
                addedNode.next = curr
                addedNode.prev = curr.prev
                curr.prev.next = addedNode
                curr.prev = addedNode
                self.length+=1
            #print(curr.prev.val);print(curr.prev.prev.val);print(self.length)


    def deleteAtIndex(self, index: int) -> None:
        if self.length == 0 and val == 0:
            pass
        elif index+1 > self.length:
            pass
        else:
            curr = traverseThis(index, self.head)
            if curr.prev != None and curr.next != None:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
            elif curr.prev == None and curr.next != None:
                self.head = curr.next
                curr.next.prev = None
            elif curr.prev != None and curr.next == None:
                curr.prev.next = None
            self.length -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)