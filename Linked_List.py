"""
A Linked List Implementation

Used to learn Leetcode


Dalice Dieckman

Date: 2024-12-11
"""

class Node:
    def __init__(self, data):
        """
        Initializes a node in the list
        """
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        """
        Initializes the LinkedList class
        """
        self.head = head
        self.count = 0


    def insert_at_start(self, data):
        """
        Inserts a new node at the start of the list
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.count +=1
            return new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.count += 1
            return new_node


    def insert_at_index(self, data, index):
        """
        Inserts a node at the given index
        """

        if index == 0:
            new_node = self.insert_at_start(data)
            self.count += 1
            return new_node

        position = 0
        current_node = self.head
        while not current_node and position+1 != index:
            # We iterate until we reach the tail (None)
            # or until we are just behind the node where the target index is.
            position += 1
            current_node = current_node.next

            if not current_node:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                self.count += 1
                return new_node

            else:
                print("Index is not present")



    def insert_at_end(self, data):
        """
        Insert node at the end of the list
        """

        new_node = Node(data)
        # If it is a new list, we insert it at the start
        if self.head is None:
            self.head = new_node
            self.count += 1
            return new_node

        current_node = self.head
        # We iterate until we reach the tail, which is None
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        self.count += 1
        return new_node


    def update_node(self, val, position):
        """
        Changes the value at a given node
        """

        current_node = self.head
        index = 0

        # If our chosen node is at the start of the list
        if index == position - 1:
            current_node.data = val
            return current_node

        else:
            # we iterate up to but not onto the index.
            # IE) As we choose node 6, it will be at index 5.
            while not current_node and index != position - 1:
                index += 1
                current_node = current_node.next

            # After iterating to the target node, we need to update its value.
            if not current_node:
                current_node.data = val
                return current_node
            else:
                print("Index not present")


    def delete_node(self, position):
        """
        Remove a node from the list
        """

        # If the list is empty we can't remove anything.
        if self.head is None:
            print("List is empty")

        current_node = self.head
        current_pos = 1
        prev_node = None

        # If we are trying to remove the first node.
        if position == 1:
            self.head = self.head.next
            self.count -= 1
            return

        else:
            # Iterate until the node
            while current_node and current_pos < position:
                prev_node = current_node
                current_node = current_node.next
                current_pos += 1

            # If the position is out of range
            if current_node is None:
                print("Position not in the list")
                return

            # Remove node when found
            prev_node.next = current_node.next
            self.count -= 1
            return


    def get_head(self):
        """
        Returns the head of the linked list as a node
        """

        current_node = self.head
        return current_node


    def get_head_val(self):
        """
        Gets the value from the head of the linked list
        """

        node = self.head
        return node.data


    def print(self):
        """
        Prints the contents of each node in the list
        """

        current_node = self.head
        list_data = []
        while current_node:
            list_data.append(current_node.data)
            current_node = current_node.next

        return print(list_data)

    def get_data_array(self):
        """
        Returns a list of each node's contents
        """

        current_node = self.head
        list_data = []
        while current_node:
            list_data.append(current_node.data)
            current_node = current_node.next

        return list_data


    def get_length(self):
        """
        Returns the length of the list
        """

        length = 0
        current_node = self.head

        if current_node is None:
            return length

        else:
            while current_node is not None:
                length += 1
                current_node = current_node.next
                
            return length