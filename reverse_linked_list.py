# Write a function that takes the head node of a linked list and 
# returns the head of a new, reversed linked list. 
# Code for class definitions comes from a Hackbright lecture.
# I wrote the rest. 

class Node(object):
    """Node in a linked list: This code taken from Hackbright lecture"""

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    """Linked List: This code taken from Hackbright lecture"""

    def __init__(self):
        self.head = None

    def print_list(self):
        """Print all items in the list."""

        current = self.head

        while current is not None:
            print current.data
            current = current.next

def reverse_ll(ll_head):
	""" Create a function to reverse a linked list.
	Accepts head node of linked list.
	Returns head node of reversed linked list.		
	"""	
	ll_head = ll_head

	if ll_head.next == None:
		return ll_head
	
	else:
		rev_ll = LinkedList()
		previous = None
		current = ll_head
		
		while current.next is not None:
			sv_orig_next = current.next
			current.next = previous
			previous = current
			current = sv_orig_next
			rev_ll.head = current
		current.next = previous
			
		return rev_ll.head

def reverse_print_linked_list():
	""" Test the reverse_ll function for 2 linked lists:
		1. Create and print a linked list with 4 nodes.
	    2. Reverse the linked list.
	    3. Print the reversed list.
	    Repeat the above 3 steps for a linked list with 1 node.
    """
# Linked list with 4 nodes: Create & print, reverse & print 	
	nodeA = Node("A")
	nodeB = Node("B")
	nodeC = Node("C")
	nodeD = Node("D")

	link_list = LinkedList()
	link_list.head = nodeA
	nodeA.next = nodeB
	nodeB.next = nodeC
	nodeC.next = nodeD

	print "Original linked list"
	link_list.print_list()
	
	rv_ll = LinkedList()
	rv_ll.head = reverse_ll(nodeA)
	
	print "Reversed linked list"
	rv_ll.print_list()

# Linked list with 1 node: Create & print, reverse & print 
	nodeZ = Node("Z")
	
	link_list_one_node = LinkedList()
	link_list_one_node.head = nodeZ

	print "Original linked list"
	link_list_one_node.print_list()
	
	rv_ll_one = LinkedList()
	rv_ll_one.head = reverse_ll(nodeZ)
	
	print "Reversed linked list"
	rv_ll_one.print_list()

if __name__ == "__main__":
	
	reverse_print_linked_list()

