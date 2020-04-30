from typing import Any, List

class Node():

    """A node in a CPA graph"""

    def __init__(self, name: str, duration: int):
        """Initialises the node

        Args:
            name: The name of the activity
            duration: The duration that it takes

        """
        self.name: str = name
        self.duration: int = duration
        self.dependencies: List['Node'] = []
        self.successors: List['Node'] = []

    def add_dependency(self, node: 'Node'):
        """Adds a dependency to another node

        Args:
            node: The node to add as a dependency

        """
        self.dependencies.append(node)

    def add_successor(self, node: 'Node'):
        """Adds a successor to another node

        Args:
            node: The node to add as a successor

        """
        self.successors.append(node)

    def forward_pass(self, default: int):
        """Calculates the forward pass information for the node.

        Args:
            default: The default value to use for the earliest start

        """
        self.earliest_start = default

        if self.dependencies:
            self.earliest_start = max(n.earliest_finish for n in self.dependencies)

        self.earliest_finish = self.earliest_start + self.duration

    def backward_pass(self, default: int):
        """Calculates the backward pass information for the node.

        Args:
            default: The default value to use for the latest finish

        """
        self.latest_finish = default

        if self.successors:
            self.latest_finish = min(n.latest_start for n in self.successors)

        self.latest_start = self.latest_finish - self.duration

    def calculate_float(self, default: int):
        """Calculates the free and total floats for the node.

        Args:
            default: The default value to use if the node has no successors

        """
        self.total_float = self.latest_finish - self.earliest_finish

        if not self.successors:
            self.free_float = default - self.earliest_finish
        else:
            self.free_float = min(s.earliest_start for s in self.successors) - self.earliest_finish

    def to_list(self) -> List[Any]:
        """Gets the contents of the node as a list so it can be used for
        DataFrames.

        Returns: A list containing the name and information about the node that
        has been calculated

        """
        return [
            self.name,
            self.earliest_start,
            self.earliest_finish,
            self.latest_start,
            self.latest_finish,
            self.total_float,
            self.free_float
        ]
