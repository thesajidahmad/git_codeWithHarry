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
            curr_node = self.head
            while(curr_node.next != None):
                curr_node = curr_node.next
            curr_node.next = new_node

    def traversal(self):
        if(self.head == None):
            print("Linked list is empty")
        else:
            curr_node = self.head
            while(curr_node != None):
                print(curr_node.data, end=" ")
                curr_node = curr_node.next

    def insertAt(self, value, position):
        new_node = Node(value)
        if (position == 0):
            new_node.next = self.head
            self.head = new_node

        else:
            count = 0
            curr_node = self.head
            prev_node = None
            while(curr_node != None and count < position):
                prev_node = curr_node
                curr_node = curr_node.next
                count += 1
            prev_node.next = new_node
            new_node.next = curr_node




sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.insertAt(5,2)
sll.traversal()