class BinaryTreeNode:
    """ Note: Class definition copied from instructions for exercise 8,
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

def is_super_balanced(binary_tree_node):
    """ Check if binary tree is super balanced
        A tree is "superbalanced" if the difference between the
        depths of any two leaf nodes is no greater than one.
        
        Arguments: 
        binary_tree_node [BinaryTreeNode] 
        
        Returns: [Boolean] True or False
    """
    depth = 0
    to_visit = [(binary_tree_node, depth)]
    min_leaf_depth = None
    max_leaf_depth = None

    while to_visit:
        # Do depth first traversal, using stack, because it finds
        # leaves more quickly, allowing quicker exit in some cases
        cur_node, cur_depth = to_visit.pop()
        # Process leaf node
        # Return false when leaves more than 1 level apart found,
        # for efficiency - don't need to traverse entire tree
        if not cur_node.left and not cur_node.right:
            if min_leaf_depth == None or cur_depth < min_leaf_depth:
                min_leaf_depth = cur_depth
            if max_leaf_depth == None or cur_depth > max_leaf_depth:
                max_leaf_depth = cur_depth
            if max_leaf_depth - min_leaf_depth > 1:
                return False
        else:
            if cur_node.left:
                to_visit.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                to_visit.append((cur_node.right, cur_depth + 1))

    return True

# Test cases
node_j = BinaryTreeNode("J")

# Binary Tree Node has no leaves
print("Node with no leaves is super balanced", "\n", "Expect: True", 
    "\n", "Actual:", is_super_balanced(node_j))
print()

node_i = node_j.insert_left("I")

# Binary tree has only 1 leaf (left)
print("Node with only 1 descendant (left) is super balanced", "\n", "Expect: True", 
    "\n", "Actual:", is_super_balanced(node_j))
print()

# Node has 2 leaves, both at same level
node_k = node_j.insert_right("K") 
print("Node with 2 descendants (left and right) is super balanced", "\n", "Expect: True", 
    "\n", "Actual:", is_super_balanced(node_j))
print()

# Node has 2 leaves, 1 level apart
node_l = node_k.insert_right("L") 
print("Node with 2 leaves, 1 level apart, is super balanced", "\n", "Expect: True", 
    "\n", "Actual:", is_super_balanced(node_j))
print()

# Node has 2 leaves, 2 levels apart
node_m = node_l.insert_right("M") 
print("Node with 2 leaves, 2 levels apart, is not super balanced", "\n", "Expect: False", 
    "\n", "Actual:", is_super_balanced(node_j))
print()

# Node has many leaves, some 2+ levels 
node_20 = BinaryTreeNode("20")
node_25 = node_20.insert_right("25")
node_18 = node_20.insert_left("18")
node_21 = node_25.insert_left("21")
node_26 = node_25.insert_right("26")
node_15 = node_18.insert_left("15")
node_12 = node_15.insert_left("12")
node_11 = node_12.insert_left("11")
node_13 = node_12.insert_right("13")
node_10 = node_11.insert_left("10")

print("Node with 3 leaves, 2 levels apart, is not super balanced", "\n", "Expect: False", 
    "\n", "Actual:", is_super_balanced(node_20))
print()
