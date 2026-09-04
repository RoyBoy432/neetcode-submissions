def traverseThis(distance: int, lnstart: ListNode):
    x = 0; curr = lnstart
    while x < distance:
        curr = curr.next; x += 1
    return curr

class ListNode:
    def __init__(self, val: str):
        self.val = val
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)
        #self.size = 1

    def visit(self, url: str) -> None:
        addedSite = ListNode(url)
        addedSite.prev = self.curr
        self.curr.next = addedSite
        self.curr = addedSite


    def back(self, steps: int) -> str:
        x = 0
        while x < steps:
            if self.curr.prev:
                self.curr = self.curr.prev
                x += 1
            else:
                x += 1

        return self.curr.val

    def forward(self, steps: int) -> str:
        x = 0
        while x < steps:
            if self.curr.next:
                self.curr = self.curr.next
                x += 1
            else:
                x += 1

        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)