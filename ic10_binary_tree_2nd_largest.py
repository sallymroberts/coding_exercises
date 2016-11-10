class BinaryTreeNode:
    """ Note: Class definition copied from instructions for exercise 10,
        interviewcake.com
    """

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def get_second_largest_value(binary_tree_node):
    """ Get value of second largest element in binary tree
        
        Arguments: 
        binary_tree_node [BinaryTreeNode] 
        
        Returns: [Integer] Value of second largest element
    """
    # Special cases
    # Root has no children: return None
    if not binary_tree_node.right and not binary_tree_node.left:
        return None

    # Root has no right child & has a left child: return root's left child value
    if not binary_tree_node.right and binary_tree_node.left:
        return binary_tree_node.left.value

    # Initialize values from root node
    cur_node = binary_tree_node.right
    prev_node_value = binary_tree_node.value

    # Traverse root's right branch, right nodes only, to end
    while True:
        if cur_node.right:
            prev_node_value = cur_node.value
            cur_node = cur_node.right
        else:
            if cur_node.left:
                return cur_node.left.value
            else:
                return prev_node_value

# Test cases
node_10 = BinaryTreeNode("10")

# Binary Tree Node has no leaves
print("Root with no leaves returns None", "\n", "Expect: None", 
    "\n", "Actual:", get_second_largest_value(node_10))
print()

# Root has no right child and left branch has only 1 descendant
node_7 = node_10.insert_left("7") 
print("Root has no right child, and left branch has 1 descendant: returns left child", "\n", "Expect: 7", 
    "\n", "Actual:", get_second_largest_value(node_10))
print()

# Root has no right child and left branch has multiple descendants
node_5 = node_7.insert_left("5")
node_3 = node_5.insert_left("3")
print("Root has no right child, left branch has multiple descendants: ", 
    "\n", "Returns Root's left child value", 
    "\n", "Expect: 7", 
    "\n", "Actual:", get_second_largest_value(node_10))
print()

# Root with only 1 descendant on right branch returns root value
node_32 = BinaryTreeNode("32")
node_35 = node_32.insert_right("35")
node_30 = node_32.insert_left("30")
print("Root with only 1 descendant on right branch: Returns root value", 
    "\n", "Expect: 32", 
    "\n", "Actual:", get_second_largest_value(node_32))
print()

# Root with left and right branches, last right descendant has no left child, 
# Returns next to last right node value 
node_20 = BinaryTreeNode("20")
node_25 = node_20.insert_right("25")
node_18 = node_20.insert_left("18")
node_21 = node_25.insert_left("21")
node_28 = node_25.insert_right("28")
node_15 = node_18.insert_left("15")
node_12 = node_15.insert_left("12")
node_11 = node_12.insert_left("11")
node_13 = node_12.insert_right("13")
node_10 = node_11.insert_left("10")
print("Root with left and right branches, last right descendant has no left child:",
    "\n", "Returns next to last right node value", 
    "\n", "Expect: 25", 
    "\n", "Actual:", get_second_largest_value(node_20))
print()

# Root with left and right branches, last right descendant has left child, 
# Returns last right node's left child value 
node_27 = node_28.insert_left("27")


print("Root with left and right branches, last right descendant has left child:",
    "\n", "Returns last right node's left child value", 
    "\n", "Expect: 27", 
    "\n", "Actual:", get_second_largest_value(node_20))
print()