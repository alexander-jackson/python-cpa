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
            self.earliest_start = max(n.earliest_finish for n in self.dependencies)

        self.earliest_finish = self.earliest_start + self.duration

    def backward_pass(self, default):
        self.latest_finish = default

        if self.successors:
            self.latest_finish = min(n.latest_start for n in self.successors)

        self.latest_start = self.latest_finish - self.duration

    def calculate_float(self, default):
        self.total_float = self.latest_finish - self.earliest_finish

        if not self.successors:
            self.free_float = default - self.earliest_finish
        else:
            self.free_float = min(s.earliest_start for s in self.successors) - self.earliest_finish

    def to_list(self):
        return [
            self.name,
            self.earliest_start,
            self.earliest_finish,
            self.latest_start,
            self.latest_finish,
            self.total_float,
            self.free_float
        ]
