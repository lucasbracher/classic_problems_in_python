class SimpleNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class DoubleNode(SimpleNode):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.prev = None

