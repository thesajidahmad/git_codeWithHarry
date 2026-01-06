class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, value):
        new_node = Node(value)

        if(self.head == None):
            self.head = new_node
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = new_node

    def traversal(self):
        if(self.head == None):
            print("Linked List is empty")

        else:
            current = self.head
            while(current != None):
                print(current.data, end=" ")
                current = current.next
    
    def insert(self, val, position):
        new_node = Node(val)
        if(position == 0):
            new_node.next = self.head
            self.head = new_node
        else:
            count = 0
            curr_node = self.head
            pre_node = None
            while(curr_node != None and count < position):
                pre_node = curr_node
                curr_node = curr_node.next
                count += 1
            pre_node.next = new_node
            new_node.next = curr_node






sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traversal()