# The basic class definition taken from:
#   https://www.sitepoint.com/ruby-interview-questions-linked-lists-and-hash-tables/

class Node
  attr_accessor :data, :next

  def initialize(data)
    @data = data
    @next = nil
  end
end

class LinkedList
  attr_accessor :head, :tail

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
  
  def print_list(head)
    curr_node = head
    while curr_node
      puts curr_node.data
      curr_node = curr_node.next
    end
  end

  # def build_ll(arr)
  #   ll = LinkedList.new
  #   arr.each do |elem|
  #     curr_node = Node.new(elem)
  #     @head ||= curr_node
  #     @tail ||= curr_node
  #     @tail.next = curr_node unless
  #   end
  # end
end

# Create and print a linked list

ll = LinkedList.new
ll.append_node(1)
ll.print_list(ll.head)




