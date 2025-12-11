
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        def helper(current_node):
            if current_node == None:
                return 0
            else:
                return current_node.data + helper(current_node.next)
        current = self.head
        return helper(current)
        """
        TODO:
        - Use recursion to sum all node data in the list.
        - Consider a helper function that:
          1. Checks if the current node is None, and returns 0 if so.
          2. Otherwise, returns node.data + recursive call on node.next.
        - Return the total sum.
        """
        pass

    def recursive_reverse(self):
        def helper(prev, current):
            if current == None:
                return prev
            else:
                next_node = current.next
                current.next = prev
                return helper(current, next_node)
        new_head = helper(None, self.head)
        self.head = new_head
        """
        TODO:
        - Reverse the list in-place using recursion.
        - Possible approach:
          1. Use a helper function that accepts 'prev' and 'current'.
          2. Base case: if current is None, return 'prev' (new head).
          3. Otherwise, swap pointers and recurse.
        - Update 'head' to the returned new head.
        """

    def recursive_search(self, target):
        def helper(current):
            if current is None:
                return False
            elif current.data == target:
                return True
            else:
                return helper(current.next)
        return helper(self.head)
        """
        TODO:
        - Return True if 'target' is found, otherwise False, using recursion.
        - Consider a helper function that:
          1. Returns False if the current node is None.
          2. Returns True if current node's data == target.
          3. Otherwise, recurse on the next node.
        """

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
