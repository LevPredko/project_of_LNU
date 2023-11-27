from Projects.Linked_Lists.LinkedList import LinkedList
from Projects.Linked_Lists.LinkedListNode import LinkedListNode


class Deque(LinkedList):
    def pop(self):
        if self.size == 0:
            raise ValueError("Deque is empty.")

        data = self.tail.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return data

    def popleft(self):
        if self.size == 0:
            raise ValueError("Deque is empty.")

        data = self.head.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return data

    def appendleft(self, data):
        new_node = LinkedListNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def remove_lines_containing(self, keyword):
        current = self.head
        while current:
            if keyword in current.value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1
            current = current.next

    def remove(self, data):
        raise NotImplementedError("Use pop() or popleft() for removal")

def reverse_file(input_file, output_file):
    stack = Deque()
    with open(input_file, 'r') as file:
        for line in file:
            stack.append(line.strip())

    with open(output_file, 'w') as file:
        while stack.size > 0:
            file.write(stack.pop() + '\n')
