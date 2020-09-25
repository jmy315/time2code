class Node:
    def __init__(self, value: int = 0):
        self.value = value
        self.next = None
    
    def get_value(self):
        return self.value

class LinkedList:
    def __init__(self, node: Node):
        self.head = node
        self.tail = node

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def add(self, node: Node):
        self.tail.next  = node
        self.tail = node

    def is_empty(self):
        if self.head:
            return False
        return True

    def __str__(self):
        temp = self.head
        s = ''
        while temp.next:
            s += str(temp.get_value()) + ' -> '
            temp = temp.next
        return ( s + str(temp.get_value()))

n = Node()
l = LinkedList(n)
l.add(Node(1))
l.add(Node(2))
print(str(l))
print(l.is_empty())
print(l.get_head().get_value())
print(l.get_tail().get_value())
