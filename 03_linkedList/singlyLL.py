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
            print("Linked List is Empty :(")
        else:
            curr_node = self.head
            while(curr_node != None):
                print(curr_node.data, end=" ")
                curr_node = curr_node.next
            print()

    def insertAt(self, value, position):
        new_node = Node(value)
        curr_node = self.head
        prev_node = None

        if(position == 0):
            new_node.next = self.head
            self.head = new_node
            return

        else:
            count = 0
            while(curr_node != None and count < position):
                prev_node = curr_node
                curr_node = curr_node.next
                count += 1
                
            if(prev_node == None):
                print("Position out of range")
                return
            
            prev_node.next = new_node
            new_node.next = curr_node

    def delete(self, value):
        curr_node = self.head
        prev_node = None

        while(curr_node != None):
            if(curr_node.data == value):
                if(prev_node == None):
                    self.head = curr_node.next
                else:
                    prev_node.next = curr_node.next
                return

            prev_node = curr_node
            curr_node = curr_node.next

        print("Node not Found :(")
