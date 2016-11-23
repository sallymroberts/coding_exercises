class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

    def print_ll(self):
        """ Print linked list nodes' values
        """
        cur_node = self
        print("Linked List Nodes values:", end = " ")

        while cur_node:
            print(cur_node.value, end = " ")
            cur_node = cur_node.next

        print()

def reverse_linked_list(head_node):
    """ Reverse linked list in place
        Arguments:
        head_node [LinkedListNode]
        Returns:
        [LinkedListNode] new head of reversed list
    """
    if head_node == None:
        return None

    if head_node.next == None:
        return head_node

    cur_node = head_node
    prev_node = None

    while cur_node:
        if cur_node.next == None:
            cur_node.next = prev_node
            return cur_node
        else:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

# Empty linked list
print("Empty linked list")
head_node = None
new_head = reverse_linked_list(head_node)
print("Expect new_head: None")
print("Actual new_head:", new_head)

# Single node linked list
node_1 = LinkedListNode("1")
node_1.next = None
head_node = node_1

print()
print("Single element linked list")
new_head = reverse_linked_list(head_node)
print("Expect new_head.value: 1")
print("Actual new_head.value:", new_head.value)
print("Expect: Linked List Nodes values: 1")
print("Actual:", end = " ")
new_head.print_ll()

node_a = LinkedListNode("A")
node_b = LinkedListNode("B")
node_c = LinkedListNode("C")
node_d = LinkedListNode("D")
node_e = LinkedListNode("E")

node_a.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e
node_e.next = None

# 5 element linked list
print()
head_node = node_a
print("5 element linked list")
new_head = reverse_linked_list(head_node)
print("Expect new_head.value: E")
print("Actual new_head.value:", new_head.value)
print("Expect: Linked List Nodes values: E D C B A")
print("Actual:", end = " ")
new_head.print_ll()