from Nodes import SimpleNode

class Stack:
    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str:
        r = ""
        p = self.head
        while p is not None:
            r = r + "-" + str(p.data)
            p = p.next
        return r[1:]

    def insert(self, data) -> None:
        node = SimpleNode(data)
        node.next = self.head
        self.head = node

    def remove(self):
        node = self.head
        if node is not None:
            self.head = self.head.next
            data = node.data
            del node
            return data
        return None

    def destroy(self) -> None:
        while True:
            test = self.remove()
            if test is None:
                break

    def isempty(self):
        return self.head is None