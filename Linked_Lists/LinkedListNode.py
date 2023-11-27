from Linked_Lists.Node import Node


class LinkedListNode(Node):
    def __init__(self, data):
        self.next = None
        self.prev = None
        Node.__init__(self, data)

