# The basic class definition taken from:
#   https://www.sitepoint.com/ruby-interview-questions-linked-lists-and-hash-tables/

class Node
  attr_accessor :next
  attr_reader :data

  def initialize(data)
    @data = data
    @next = nil
  end
end

class LinkedList
  attr_reader :head, :tail

  def initialize
    @head = nil
    @tail = nil
  end

  # Add node with data to end of list
  def append_node(data)
    new_node = Node.new(data)
    @head ||= new_node
    @tail.next = new_node if @tail
    @tail = new_node
  end

  # Print linked list beginning with current node
  def self.print_list(curr_node)
    while curr_node
      puts curr_node.data
      curr_node = curr_node.next
    end
  end

  # Build linked list from array
  def self.build_ll(arr)
    ll = LinkedList.new
    arr.each do |elem|
      ll.append_node(elem)
    end
    ll
  end
end

# Create and print a linked list

arr = [10, 6, 4, 11, 3]
ll = LinkedList.build_ll(arr)
LinkedList.print_list(ll.head)




