class BinaryTreeNode:
    """ Note: Class definition copied from instructions for exercise 9,
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

def is_valid_binary_tree(binary_tree_node):
    """ Check if binary tree is valid
        A tree is valid if every node is positioned correctly in
        relation to its ancestors
        
        Arguments: 
        binary_tree_node [BinaryTreeNode] 
        
        Returns: [Boolean] True or False
    """
    # Store nodes to visit as tuple: (node, current max value, current min value)
    to_visit = [(binary_tree_node, None, None)]

    while to_visit:
        cur_node, cur_max, cur_min = to_visit.pop()

        # Validate current node
        if cur_max:
            if cur_node.value >= cur_max:
                return False

        if cur_min:
            if cur_node.value <= cur_min:
                return False

        # Add current node's children to nodes to visit
        # Left child: max is parent's value, min is same as parent's min 
        if cur_node.left:
            to_visit.append((cur_node.left, cur_node.value, cur_min))

        # Right child: max is same as parent's max, min is parent's value
        if cur_node.right:
            to_visit.append((cur_node.right, cur_max, cur_node.value))

    return True

# Test cases
node_j = BinaryTreeNode("J")

# Binary Tree Node has no leaves
print("Node with no leaves is valid", "\n", "Expect: True", 
    "\n", "Actual:", is_valid_binary_tree(node_j))
print()

# Node has 2 leaves, both valid
node_k = node_j.insert_right("K") 
print("Node with 2 valid leaves (left and right) is valid", "\n", "Expect: True", 
    "\n", "Actual:", is_valid_binary_tree(node_j))
print()

# Node with right leaf value less than immediate parent, is invalid
node_d = node_k.insert_right("D") 
print("Node with right leaf less than parent is invalid", "\n", "Expect: False", 
    "\n", "Actual:", is_valid_binary_tree(node_j))
print()

# Node with left leaf value greater than immediate parent, is invalid
node_58 = BinaryTreeNode("58")
node_56 = node_58.insert_left("56")
node_57 = node_56.insert_left("57") 
print("Node with left leaf greater than parent is invalid", "\n", "Expect: False", 
    "\n", "Actual:", is_valid_binary_tree(node_58))
print()

# Node with left leaf value equal to immediate parent, is invalid
node_80 = BinaryTreeNode("80")
node_79 = node_80.insert_left("79")
node_79_B = node_79.insert_left("79") 
print("Node with left leaf value equal to parent is invalid", "\n", "Expect: False", 
    "\n", "Actual:", is_valid_binary_tree(node_80))
print()

# Node with right leaf value equal to immediate parent, is invalid
node_90 = BinaryTreeNode("90")
node_92 = node_90.insert_right("92")
node_92_B = node_92.insert_right("92") 
print("Node with right leaf value equal to parent is invalid", "\n", "Expect: False", 
    "\n", "Actual:", is_valid_binary_tree(node_90))
print()

# Node has several left and right descendants, all valid 
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

print("Node with several valid left and right descendants is valid", "\n", "Expect: True", 
    "\n", "Actual:", is_valid_binary_tree(node_20))
print()

# Node with left leaf value greater than parent, is invalid
node_22 = node_21.insert_left("22")
print("Node with left leaf value greater than parent is invalid", "\n", "Expect: False", 
    "\n", "Actual:", is_valid_binary_tree(node_20))
print()

# Left branch from ancestor has right leaf greater than ancestor, is invalid
node_44 = BinaryTreeNode("44")
node_40 = node_44.insert_left("40")
node_46 = node_40.insert_right("46")
print("Left branch from ancestor has right leaf greater than ancestor: is invalid", "\n", "Expect: False", 
    "\n", "Actual:", is_valid_binary_tree(node_44))
print()

# Right branch from ancestor has right left greater than ancestor, is invalid
node_64 = BinaryTreeNode("64")
node_70 = node_64.insert_right("70")
node_60 = node_70.insert_left("60")
print("Right branch from ancestor has left leaf less than ancestor: is invalid", "\n", "Expect: False", 
    "\n", "Actual:", is_valid_binary_tree(node_64))
print()
