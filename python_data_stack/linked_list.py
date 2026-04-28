class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

if __name__ == "__main__":
    obj_1=Node(10)
    print(obj_1.data)
    obj_2=Node(20)
    print(obj_2.data)
    l1=LinkedList()
    l1.insert_at_beginning(1)
    print(l1.head.data)
  