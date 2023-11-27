from Linked_Lists.LinkedListNode import LinkedListNode


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def find(self, data):
        current = self.head
        index = 0
        while current:
            if current.value == data:
                return index
            current = current.next
            index += 1
        raise ValueError("Node with the specified data not found or the list is empty.")

    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of range.")
        current = self.head
        for _ in range(i):
            current = current.next
        return current

    def __len__(self):
        return self.size

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(repr(current.value))
            current = current.next
        return "[" + ", ".join(result) + "]"

    def remove(self, data):
        target = self.find(data)
        if target.prev:
            target.prev.next = target.next
        else:
            self.head = target.next
        if target.next:
            target.next.prev = target.prev
        else:
            self.tail = target.prev
        self.size -= 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range.")
        if index == self.size:
            self.append(data)
        else:
            new_node = LinkedListNode(data)
            if index == 0:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                current = self.get(index)
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
            self.size += 1