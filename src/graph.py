import subprocess
from typing import Dict

import pandas as pd

from node import Node

class Graph():

    """A graph that we want to perform CPA on. """

    def __init__(self, activities: Dict):
        """Initialises the Graph object

        Args:
            activities: JSON data in the format shown in `activities.json`
            describing the names, durations and dependencies for the problem

        """
        self.nodes = {}
        self.generate_graph(activities)

    def generate_graph(self, activities: Dict):
        """Generates the nodes of the graph.

        """
        keys = list(activities.keys())

        for key in keys:
            node = Node(key, activities[key]["duration"])
            self.nodes[key] = node

        for key in keys:
            for dependency in activities[key]["dependencies"]:
                self.nodes[key].add_dependency(self.nodes[dependency])
                self.nodes[dependency].add_successor(self.nodes[key])

    def forward_pass(self):
        """Calculates the forward pass for the graph.

        """
        completed = []

        while len(completed) != len(self.nodes):
            possible = [
                n for n in self.nodes.values() if
                all(d in completed for d in n.dependencies)
                and
                n not in completed
            ]

            for node in possible:
                node.forward_pass(0)
                completed.append(node)

    def backward_pass(self):
        """Calculates the backward pass for the graph after a forward pass has
        been complete.

        """
        completed = []

        leaves = [n for n in self.nodes.values() if not n.successors]
        highest_early_finish = max(l.earliest_finish for l in leaves)

        while len(completed) != len(self.nodes):
            possible = [
                n for n in self.nodes.values() if
                all(d in completed for d in n.successors)
                and
                n not in completed
            ]

            for node in possible:
                node.backward_pass(highest_early_finish)
                completed.append(node)

    def calculate_floats(self):
        """Calculates the free and total floats for the graph after a forward
        and backward pass.

        """
        leaves = [n for n in self.nodes.values() if not n.successors]
        highest_early_finish = max(l.earliest_finish for l in leaves)

        for node in self.nodes.values():
            node.calculate_float(highest_early_finish)

    def display_calculated_values(self):
        """Displays a formatted table with the different values calculated
        after the algorithm has finished.

        """
        data = [n.to_list() for n in self.nodes.values()]
        terminal_width = int(subprocess.check_output(['stty', 'size']).split()[1])

        if terminal_width >= 100:
            columns = ["name",
                       "earliest start", "earliest finish",
                       "latest start", "latest finish",
                       "total float", "free float"]
        else:
            columns = ["name", "es", "ef", "ls", "lf", "tf", "ff"]

        frame = pd.DataFrame(data, columns=columns)
        print(frame)
