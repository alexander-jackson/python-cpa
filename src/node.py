class Node(object):

    """A node in a CPA graph"""

    def __init__(self, name, duration):
        """Initialises the node

        Args:
            name: TODO
            duration: TODO
            dependencies: TODO

        """
        self.name = name
        self.duration = duration
        self.dependencies = []

    def add_dependency(self, node):
        """Adds a dependency to another node

        Args:
            node (TODO): TODO

        Returns: TODO

        """
        self.dependencies.append(node)

    def forward_pass(self):
        """Calculates the forward pass for the node
        Returns: TODO

        """
        self.earliest_start = 0

        if self.dependencies:
            key = lambda n: n.earliest_finish
            lowest = max(self.dependencies, key=key)
            self.earliest_start = lowest.earliest_finish

        self.earliest_finish = self.earliest_start + self.duration
