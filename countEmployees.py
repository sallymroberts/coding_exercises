# Hackbright exercise to practice trees by counting employees
# in an org chart tree, with doctests provided.
# I coded the count_employees function.

class Node(object):
    """Node in a tree."""

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def count_employees(self):
        """Return a count of how many employees this person manages.

        Return a count of how many people that manager manages. This should
        include *everyone* under them, not just people who directly report to
        them.

        Our organization has the following org chart:

                        Jane
              Jessica          Janet
           Al  Bob  Jen     Nick  Nora
                                    Henri

        >>> henri = Node("Henri")
        >>> nora = Node("Nora", [henri])
        >>> nick = Node("Nick")
        >>> janet = Node("Janet", [nick, nora])
        >>> al = Node("Al")
        >>> bob = Node("Bob")
        >>> jen = Node("Jen")
        >>> jessica = Node("Jessica", [al, bob, jen])
        >>> jane = Node("Jane", [jessica, janet])

        >>> henri.count_employees()
        0

        >>> nora.count_employees()
        1

        >>> jane.count_employees()
        8
        """
    
        emps = [self]
        count = 0

        while emps:
            emp_node = emps.pop()
            for child in emp_node.children:
                count += 1
                emps.append(child)

        return count

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ARE A TREE GENIUS!\n"
