"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
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
            # self.length = self.length - 1
            return current_tail.value
        # Check if it's there
        # General case:
        else:
        # Start at head and iterate to the next-to-last node
            current_node = self.head
        # Stop when current_node.next == self.tail
            while current_node.next_node != self.tail:
                current_node = current_node.next_node
            # Once we exit the while loop, current_node is pointing to the node right before self.tail
        # Save the current_tail value
            current_tail = self.tail
        # Set self.tail to current_node
            self.tail = current_node
        # Set current_node.next to None
            current_node.next_node = None
            # self.length = self.length - 1
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

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size < 1:
            return None
        self.size -= 1
        self.storage.remove_head()
    
    def get_value(self):
        current = self.storage.head
        while current is not None:
            print(current.value)
            current = current.next_node


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
            
        self.size -= 1
        value = self.storage.remove_head()
        return value


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                new_node = BSTNode(value)
                self.right = new_node
            else:
                self.right.insert(value)

        if value < self.value:
            if self.left is None:
                new_node = BSTNode(value)
                self.left = new_node
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        
        if self.right:
            self.right.for_each(fn)

    # def for_each_iterative(self, fn):
    #     # Depth first traversal iterative:
    #     # Start at the root
    #     cur_node = self
    #     # Push it on to the stack
    #     stack = Stack()
    #     stack.push(cur_node)
    #     #
    #     # While stack is not empty:
    #     while len(stack) > 0:
    #         cur_node = stack.pop()
    #     #     Push right
    #         if cur_node.right is not None:
    #             stack.push(cur_node.right)
    #     #     Push left
    #         if cur_node.left is not None:
    #             stack.push(cur_node.left)
    #     #     Do the thing with the current node
    #         fn(cur_node.value)
    
    # def breadth_first_traversal(self, fn):
    #     pass
    #     # Start at the root
    #     # Push it onto the queue
    #     #
    #     # While queue is not empty:
    #     # Cur_node = Remove from the queue
    #     # Add cur_node children to the queue
    #     # Process cur_node

    # # Part 2 -----------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     #start at root node
    #     cur_node = self
    #     if cur_node:
    #         in_order_print(cur_node.left)

    #         print(cur_node.value)

    #         in_order_print(cur_node.right)

        

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     pass

    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass

    # def breadth_first_traversal(self, fn):


