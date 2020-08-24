    def remove_tail(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            value = self.tail
            self.head = None
            self.tail = None
            return value
        second_last = self.head
        prev_tail = self.tail
        else:
            while(second_last.next_node.next_node):
                second_last = second_last.next_node
            self.tail = second_last
            self.tail.next_node = None
        return prev_tail