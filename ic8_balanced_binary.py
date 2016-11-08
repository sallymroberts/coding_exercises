class BinaryTreeNode:

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
        cur_node, cur_depth = to_visit.pop(0)
        # Process leaf node
        if not cur_node.left and not cur_node.right:
            if min_leaf_depth == None or cur_depth < min_leaf_depth:
                min_leaf_depth = cur_depth
            if max_leaf_depth == None or cur_depth > max_leaf_depth:
                max_leaf_depth = cur_depth
            if max_leaf_depth - min_leaf_depth > 1:
                # print("cur_node.value:", cur_node.value)
                return False
        else:
            if cur_node.left:
                to_visit.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                to_visit.append((cur_node.right, cur_depth + 1))

    return True

# Test cases
node_a = BinaryTreeNode("A")

# Binary Tree Node has no leaves
print("Node with no leaves is super balanced", "\n", "Expect: True", 
    "\n", "Actual:", is_super_balanced(node_a))
print()

node_c = node_a.insert_left("C")

# Binary tree has only 1 leaf (left)
print("Node with only 1 descendant (left) is super balanced", "\n", "Expect: True", 
    "\n", "Actual:", is_super_balanced(node_a))
print()

# Node has 2 leaves, both at same level
node_b = node_a.insert_right("B") 
print("Node with 2 descendants (left and right) is super balanced", "\n", "Expect: True", 
    "\n", "Actual:", is_super_balanced(node_a))
print()

# Node has 2 leaves, 1 level apart
node_d = node_b.insert_right("D") 
print("Node with 2 leaves, 1 level apart, is super balanced", "\n", "Expect: True", 
    "\n", "Actual:", is_super_balanced(node_a))
print()

# Node has 2 leaves, 2 levels apart
node_d = node_d.insert_right("E") 
print("Node with 2 leaves, 2 levels apart, is not super balanced", "\n", "Expect: False", 
    "\n", "Actual:", is_super_balanced(node_a))
print()

# Node has many leaves, some 2+ levels 
node_1 = BinaryTreeNode("1")
node_2 = node_1.insert_right("2")
node_3 = node_1.insert_left("3")
node_4 = node_3.insert_left("4")
node_5 = node_3.insert_right("5")
node_6 = node_2.insert_left("6")
node_7 = node_6.insert_left("7")
node_8 = node_7.insert_left("8")
node_10 = node_7.insert_right("10")
node_9 = node_8.insert_left("9")

print("Node with 3 leaves, 2 levels apart, is not super balanced", "\n", "Expect: False", 
    "\n", "Actual:", is_super_balanced(node_1))
print()
