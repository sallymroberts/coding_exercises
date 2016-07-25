# exercises with trees

# Node class for tree
class Node
  attr_accessor :data, :children

  def initialize(data, children)
    @data = data
    if children
      @children = children
    else
      @children = []
    end
    # @children = []
  end

  # Add children to node
  # @param [Array] more_children array of child nodes
  def add_children(more_children)
    @children.push(*more_children)
  end

  # Print node and all its descendants
  # @param [Node] curr_node
  def self.print_nodes(curr_node)
    to_visit = [curr_node]

    while to_visit != []
      curr_node = to_visit.pop
      puts curr_node.data
      to_visit += curr_node.children
    end
  end

  # Check if node exists with specified data
  # @param [Node] curr_node node to begin search
  # @param [String] data to check for
  def self.node_exists?(curr_node, data)
    to_visit = [curr_node]

    while to_visit != []
      curr_node = to_visit.pop

      if curr_node.data == data
        return true
      else
        to_visit += curr_node.children
      end
    end
  end
end

# Tree class, composed of node(s)
class Tree
  attr_reader :root

  # @param [Node] root node
  def initialize(root)
    @root = root
  end
end

# Tests of Tree and Node classes
mary = Node.new("Mary", [])
dan = Node.new("Dan", [])
sam = Node.new("Sam", [mary, dan])

Node.print_nodes(sam)

puts
ralph = Node.new("Ralph", [])
mary.add_children([ralph])
Node.print_nodes(sam)
puts
sam_family = Tree.new(sam)
Node.print_nodes(sam_family.root)

puts "Ralph exists in Sam's family?: #{Node.node_exists?(sam, "Ralph")}"