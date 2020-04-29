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
        self.successors = []

    def add_dependency(self, node):
        """Adds a dependency to another node

        Args:
            node (TODO): TODO

        Returns: TODO

        """
        self.dependencies.append(node)

    def add_successor(self, node):
        """Adds a successor to another node

        Args:
            node (TODO): TODO

        Returns: TODO

        """
        self.successors.append(node)

    def forward_pass(self, default):
        """Calculates the forward pass for the node
        Returns: TODO

        """
        self.earliest_start = default

        if self.dependencies:
            key = lambda n: n.earliest_finish
            lowest = max(self.dependencies, key=key)
            self.earliest_start = lowest.earliest_finish

        self.earliest_finish = self.earliest_start + self.duration

    def backward_pass(self, default):
        self.latest_finish = default

        if self.successors:
            key = lambda n: n.latest_start
            lowest = max(self.successors, key=key)
            self.latest_finish = lowest.latest_start

        self.latest_start = self.latest_finish - self.duration
