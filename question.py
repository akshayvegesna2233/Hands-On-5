class MinPriorityQueue:
    def __init__(self):
        self.queue = []

    @staticmethod
    def parent_idx(child_idx):
        """Compute parent index using bitwise operation."""
        return (child_idx - 1) >> 1

    @staticmethod
    def left_child_idx(parent_idx):
        """Compute left child index using bitwise operation."""
        return (parent_idx << 1) + 1

    @staticmethod
    def right_child_idx(parent_idx):
        """Compute right child index using bitwise operation."""
        return (parent_idx << 1) + 2

    def bubble_down(self, start_idx):
        """Adjust heap downwards to maintain min-heap property."""
        min_idx = start_idx
        left = self.left_child_idx(start_idx)
        right = self.right_child_idx(start_idx)

        if left < len(self.queue) and self.queue[left] < self.queue[min_idx]:
            min_idx = left

        if right < len(self.queue) and self.queue[right] < self.queue[min_idx]:
            min_idx = right

        if min_idx != start_idx:
            self.queue[start_idx], self.queue[min_idx] = self.queue[min_idx], self.queue[start_idx]
            self.bubble_down(min_idx)

    def construct_heap(self, input_list):
        """Construct a min heap from an input list."""
        self.queue = input_list[:]
        for i in range(len(input_list) // 2, -1, -1):
            self.bubble_down(i)

    def pop_min(self):
        """Remove and return the minimum element from the heap."""
        if not self.queue:
            return None
        if len(self.queue) == 1:
            return self.queue.pop()

        min_element = self.queue[0]
        self.queue[0] = self.queue.pop()
        self.bubble_down(0)
        return min_element

    def add(self, item):
        """Add a new item to the heap."""
        self.queue.append(item)
        self.bubble_up(len(self.queue) - 1)

    def bubble_up(self, idx):
        """Adjust heap upwards to maintain min-heap property."""
        while idx > 0 and self.queue[self.parent_idx(idx)] > self.queue[idx]:
            parent = self.parent_idx(idx)
            self.queue[idx], self.queue[parent] = self.queue[parent], self.queue[idx]
            idx = parent

def comprehensive_showcase():
    print("Comprehensive MinPriorityQueue Showcase")
    print("======================================")

    # Integer example
    print("\n1. Integer MinPriorityQueue:")
    int_pq = MinPriorityQueue()
    int_data = [4, 10, 3, 5, 1, 1]
    int_pq.construct_heap(int_data)
    print("Initial heap:", int_pq.queue)
    int_pq.add(2)
    print("After adding 2:", int_pq.queue)
    print("Popped minimum:", int_pq.pop_min())
    print("Heap after pop:", int_pq.queue)

    # Float example
    print("\n2. Float MinPriorityQueue:")
    float_pq = MinPriorityQueue()
    float_data = [4.5, 10.1, 3.3, 5.7, 1.0]
    float_pq.construct_heap(float_data)
    print("Initial heap:", float_pq.queue)
    float_pq.add(2.2)
    print("After adding 2.2:", float_pq.queue)
    print("Popped minimum:", float_pq.pop_min())
    print("Heap after pop:", float_pq.queue)

    # Custom data structure example
    print("\n3. Custom Data Structure (Employee) MinPriorityQueue:")
    class Employee:
        def __init__(self, name, rank):
            self.name = name
            self.rank = rank
        def __lt__(self, other):
            return self.rank < other.rank
        def __repr__(self):
            return f"Employee({self.name}, {self.rank})"

    employee_pq = MinPriorityQueue()
    employees = [Employee("Alice", 3), Employee("Bob", 2), Employee("Charlie", 4), Employee("David", 1)]
    employee_pq.construct_heap(employees)
    print("Initial heap:", employee_pq.queue)
    employee_pq.add(Employee("Eve", 2))
    print("After adding Eve:", employee_pq.queue)
    print("Popped minimum:", employee_pq.pop_min())
    print("Heap after pop:", employee_pq.queue)

if __name__ == "__main__":
    comprehensive_showcase()


"""
Comprehensive MinPriorityQueue Showcase
======================================

1. Integer MinPriorityQueue:
Initial heap: [1, 4, 1, 5, 10, 3]
After adding 2: [1, 4, 1, 5, 10, 3, 2]
Popped minimum: 1
Heap after pop: [1, 4, 2, 5, 10, 3]

2. Float MinPriorityQueue:
Initial heap: [1.0, 4.5, 3.3, 5.7, 10.1]
After adding 2.2: [1.0, 4.5, 2.2, 5.7, 10.1, 3.3]
Popped minimum: 1.0
Heap after pop: [2.2, 4.5, 3.3, 5.7, 10.1]

3. Custom Data Structure (Employee) MinPriorityQueue:
Initial heap: [Employee(David, 1), Employee(Bob, 2), Employee(Charlie, 4), Employee(Alice, 3)]
After adding Eve: [Employee(David, 1), Employee(Bob, 2), Employee(Charlie, 4), Employee(Alice, 3), Employee(Eve, 2)]
Popped minimum: Employee(David, 1)
Heap after pop: [Employee(Eve, 2), Employee(Bob, 2), Employee(Charlie, 4), Employee(Alice, 3)]"""