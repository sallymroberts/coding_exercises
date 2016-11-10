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

def get_largest_value(binary_tree_node):
    """ Get largest value in binary tree
        Arguments: 
        binary_tree_node [BinaryTreeNode] 
        
        Returns: Value of largest element
    """
    cur_node = binary_tree_node

    # Traverse root's right branch, right nodes only, to end
    while True:
        if cur_node.right:
            cur_node = cur_node.right
        else:
            return cur_node.value

def get_second_largest_value(binary_tree_node):
    """ Get value of second largest element in binary tree
        
        Arguments: 
        binary_tree_node [BinaryTreeNode] 
        
        Returns: Value of second largest element
                 None, if no second largest element
    """
    # Root has no descendants
    if not binary_tree_node.right and not binary_tree_node.left:
        return None
    # Root has left child and no right child: get root's left branch largest value
    elif not binary_tree_node.right:
        return get_largest_value(binary_tree_node.left)
    # Root has right child
    else:
        # Initialize values from binary_tree_node
        cur_node = binary_tree_node
        prev_node_value = None

        # Traverse root's right branch, right nodes only, to end
        while True:
            if cur_node.right:
                prev_node_value = cur_node.value
                cur_node = cur_node.right
            else:
                # Found last right node (largest value), return next largest value
                if cur_node.left:
                    return get_largest_value(cur_node.left)
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

# Root has no right child and 
# root's left child has left child and no right child
node_5 = node_7.insert_left("5")
node_3 = node_5.insert_left("3")
print("Root has no right child,", 
    "and root's left child has left child and no right child: ", 
    "\n", "Returns Root's left child value", 
    "\n", "Expect: 7", 
    "\n", "Actual:", get_second_largest_value(node_10))
print()

# Root has no right child
# Root's left child has left and multiple right descendants
# Returns root's left child's last right descendant
node_8 = node_7.insert_right("8")
node_9 = node_8.insert_right("9")

print("Root has no right child",
    "\n", "Root's left child has left and multiple right descendants",
    "\n", "Returns root's left child's last right descendant",  
    "\n", "Expect: 9", 
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
node_26 = node_28.insert_left("26")
node_27 = node_26.insert_right("27")


print("Root with left and right branches, last right descendant has left child:",
    "\n", "Returns last right descendant's left child's last right descendant", 
    "\n", "Expect: 27", 
    "\n", "Actual:", get_second_largest_value(node_20))
print()