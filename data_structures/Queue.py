from Nodes import DoubleNode
from Stack import Stack

class Queue(Stack):
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self, data) -> None:
        node = DoubleNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
