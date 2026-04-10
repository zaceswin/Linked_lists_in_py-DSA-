"""
Week 5 Linked List Assignment
Name: Zack Mutitu Macharia

Description:
Complete implementation of a singly linked list with:
- Required operations
- Extra advanced methods
- Proper documentation
- Test cases
"""


class Node:
    """Represents a single node in the linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Represents a singly linked list"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check if list is empty (O(1))"""
        return self.head is None

    def size(self):
        """Return number of nodes (O(n))"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def prepend(self, data):
        """Insert at beginning (O(1))"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        """Insert at end (O(n))"""
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def insert_at_position(self, data, pos):
        """Insert at specific position (O(n))"""
        if pos < 0:
            raise IndexError("Invalid position")

        if pos == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head

        for _ in range(pos - 1):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next

        if current is None:
            raise IndexError("Position out of bounds")

        new_node.next = current.next
        current.next = new_node

    def delete_by_value(self, value):
        """Delete first occurrence of value (O(n))"""
        if self.is_empty():
            print("List is empty")
            return False

        if self.head.data == value:
            self.head = self.head.next
            return True

        current = self.head

        while current.next and current.next.data != value:
            current = current.next

        if current.next is None:
            print("Value not found")
            return False

        current.next = current.next.next
        return True

    def search(self, value):
        """Search value and return index (O(n))"""
        current = self.head
        index = 0

        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1

        return -1

    def display(self):
        """Display list (O(n))"""
        if self.is_empty():
            print("List is empty")
            return

        current = self.head
        elements = []

        while current:
            elements.append(str(current.data))
            current = current.next

        print(" -> ".join(elements) + " -> None")

    # ========================
    # EXTRA FUNCTIONS (BONUS)
    # ========================

    def reverse(self):
        """Reverse the list (O(n))"""
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def find_middle(self):
        """Find middle element (O(n))"""
        if self.is_empty():
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def detect_cycle(self):
        """Detect cycle using Floyd's algorithm (O(n))"""
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# ===========================
# TEST CASES (VERY IMPORTANT)
# ===========================
if __name__ == "__main__":

    print("=== TEST CASES ===")

    # Test 1: Empty list
    print("\nTest 1: Empty List")
    ll = LinkedList()
    ll.display()
    print("Is empty:", ll.is_empty())

    # Test 2: Prepend & Append
    print("\nTest 2: Prepend & Append")
    ll.prepend(10)
    ll.prepend(20)
    ll.append(30)
    ll.append(40)
    ll.display()

    # Test 3: Insert at position
    print("\nTest 3: Insert at Position")
    ll.insert_at_position(25, 2)
    ll.display()

    # Test 4: Delete by value
    print("\nTest 4: Delete by Value")
    ll.delete_by_value(25)
    ll.display()

    # Test 5: Search
    print("\nTest 5: Search")
    print("Index of 30:", ll.search(30))
    print("Index of 100:", ll.search(100))

    # Test 6: Size
    print("\nTest 6: Size")
    print("Size:", ll.size())

    # Test 7: Delete head
    print("\nTest 7: Delete Head")
    ll.delete_by_value(20)
    ll.display()

    # Test 8: Reverse
    print("\nTest 8: Reverse")
    ll.reverse()
    ll.display()

    # Test 9: Find middle
    print("\nTest 9: Find Middle")
    print("Middle element:", ll.find_middle())

    # Test 10: Detect cycle (no cycle)
    print("\nTest 10: Detect Cycle (No cycle)")
    print("Cycle exists:", ll.detect_cycle())

    # Test 11: Create cycle and detect
    print("\nTest 11: Create Cycle and Detect")
    if ll.head and ll.head.next and ll.head.next.next:
        ll.head.next.next.next = ll.head  # create cycle
    print("Cycle exists after creating loop:", ll.detect_cycle())
