class QueueTwoStacks():
    """ Create queue from 2 stacks
        Optimize for time cost of mm function calls on queue.
        These can be any mix of enqueue and dequeue calls
    """

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        # move all elements from stack 2 to stack 1    
        while len(self.stack2) > 0:
            elem = self.stack2.pop()
            self.stack1.append(elem)
        # add element to stack 1
        self.stack1.append(item)

    def dequeue(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            raise Exception("Can't dequeue from empty queue")
        # move all but last element from stack1 to stack 2
        while len(self.stack1) > 0:
            elem = self.stack1.pop()
            self.stack2.append(elem)
        # pop element at index 0 from stack 1
        self.stack2.pop()

# Tests
print("*" * 80)
num_queue = QueueTwoStacks()
num_queue.enqueue(1)
print("Enqueue 1, resulting stack1, stack2: ", "\n", 
    "Expect: [1] []", "\n", 
    "Actual:", num_queue.stack1, num_queue.stack2)
print()

num_queue.enqueue(2)
print("Enqueue 2, resulting stack1, stack2: ", "\n", 
    "Expect: [1, 2] []", "\n", 
    "Actual:", num_queue.stack1, num_queue.stack2)
print()

num_queue.enqueue(3)
print("Enqueue 3, resulting stack1, stack2: ", "\n", 
    "Expect: [1, 2, 3] []", "\n", 
    "Actual:", num_queue.stack1, num_queue.stack2)
print()

num_queue.enqueue(4)
print("Enqueue 4, resulting stack1, stack2: ", "\n", 
    "Expect: [1, 2, 3, 4] []", "\n", 
    "Actual:", num_queue.stack1, num_queue.stack2)
print()

num_queue.enqueue(5)
print("Enqueue 5, resulting stack1, stack2: ", "\n", 
    "Expect: [1, 2, 3, 4, 5] []", "\n", 
    "Actual:", num_queue.stack1, num_queue.stack2)
print()

num_queue.dequeue()
print("Dequeue, resulting stack1, stack2: ", "\n", 
    "Expect: [] [5, 4, 3, 2]", "\n", 
    "Actual:", num_queue.stack1, num_queue.stack2)
print()

num_queue.dequeue()
print("Dequeue, resulting stack1, stack2: ", "\n", 
    "Expect: [] [5, 4, 3]", "\n", 
    "Actual:", num_queue.stack1, num_queue.stack2)
print()

num_queue.enqueue(6)
print("Enqueue 6, resulting stack1, stack2: ", "\n", 
    "Expect: [3, 4, 5, 6] []", "\n", 
    "Actual:", num_queue.stack1, num_queue.stack2)
print()

num_queue.dequeue()
print("Dequeue, resulting stack1, stack2: ", "\n", 
    "Expect: [] [6, 5, 4]", "\n", 
    "Actual:", num_queue.stack1, num_queue.stack2)
print()

num_queue.dequeue()
print("Dequeue, resulting stack1, stack2: ", "\n", 
    "Expect: [] [6, 5]", "\n", 
    "Actual:", num_queue.stack1, num_queue.stack2)
print()

num_queue.dequeue()
print("Dequeue, resulting stack1, stack2: ", "\n", 
    "Expect: [] [6]", "\n", 
    "Actual:", num_queue.stack1, num_queue.stack2)
print()

num_queue.dequeue()
print("Dequeue, resulting stack1, stack2: ", "\n", 
    "Expect: [] []", "\n", 
    "Actual:", num_queue.stack1, num_queue.stack2)
print()

print("Expect Exception: Can't dequeue from empty queue")
num_queue.dequeue()