class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    

class LinkedList:
    def __init__(self):
        self.head = None  
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value 

    def remove_tail(self):
        # Remove Tail:
        if self.tail is None:
            return None
        # List of 1 element:
        if self.head == self.tail:
        # Save the current_tail.value
            current_tail = self.tail
        # Set self.tail to None
            self.tail = None
        # Set self.head to None
            self.head = None
            self.length = self.length - 1
            return current_tail.value
        # Check if it's there
        # General case:
        else:
        # Start at head and iterate to the next-to-last node
            current_node = self.head
        # Stop when current_node.next == self.tail
            while current_node.next != self.tail:
                current_node = current_node.next
            # Once we exit the while loop, current_node is pointing to the node right before self.tail
        # Save the current_tail value
            current_tail = self.tail
        # Set self.tail to current_node
            self.tail = current_node
        # Set current_node.next to None
            current_node.next = None
            self.length = self.length - 1
            return current_tail.value

    def contains(self, value):
        if self.head is None:
            return False
        
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True

            current_node = current_node.next_node
        return False 
