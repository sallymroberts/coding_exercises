class LinkedListNode:
    """Linked List Node with attributes value and next."""
    def __init__(self, value, next):
        self.value = value
        self.next  = next

def contains_cycle(first_node):
	"""
	Determine if a linked list has a cycle.

	A cycle occurs when a node’s next points back to a 
	previous node in the list.

	Arguments: 
		first_node [LinkedListNode] first node in linked list 
	Returns Boolean: 
		True  - linked list has cycle 
		False - linked list does not have cycle
	"""
	nodes = {first_node}
	cur_node = first_node

	while cur_node:
		if not cur_node.next:
			return False
		elif cur_node.next in nodes:
			return True
		else:
			nodes.add(cur_node.next)
			cur_node = cur_node.next

# Construct and test valid linked list without a cycle
node_4 = LinkedListNode("4", None)
node_3 = LinkedListNode("3", node_4)
node_2 = LinkedListNode("2", node_3)
node_1 = LinkedListNode("1", node_2)

is_cycle = contains_cycle(node_1)
print("is_cycle (should be False):", is_cycle)

# Construct and test invalid linked list with a cycle
node_d = LinkedListNode("D", None)
node_c = LinkedListNode("C", node_d)
node_b = LinkedListNode("B", node_c)
node_a = LinkedListNode("A", node_b)
node_d.next = node_c

is_cycle = contains_cycle(node_a)
print("is_cycle (should be True):", is_cycle)

# Construct and test invalid linked list with one node 
# pointing to itself as next
node_e = LinkedListNode("E", None)
node_e.next = node_e

is_cycle = contains_cycle(node_e)
print("is_cycle (should be True):", is_cycle)