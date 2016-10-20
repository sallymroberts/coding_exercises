class LinkedListNode:

    def __init__(self, value, next):
        self.value = value
        self.next  = next

def is_cycle_ll(first_node):
	""" 
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

node_4 = LinkedListNode("4", None)
node_3 = LinkedListNode("3", node_4)
node_2 = LinkedListNode("2", node_3)
node_1 = LinkedListNode("1", node_2)

is_cycle = is_cycle_ll(node_1)
print("is_cycle (should be False):", is_cycle)

node_d = LinkedListNode("D", None)
node_c = LinkedListNode("C", node_d)
node_b = LinkedListNode("B", node_c)
node_a = LinkedListNode("A", node_b)
node_d.next = node_a

is_cycle = is_cycle_ll(node_a)
print("is_cycle (should be True):", is_cycle)