from node import Node

class Graph(object):

    """A graph that we want to perform CPA on. """

    def __init__(self, activities):
        """Initialises the Graph object

        Args:
            activities: TODO

        """
        self.nodes = {}
        self.generate_graph(activities)

    def generate_graph(self, activities):
        """Generates the nodes of the graph
        Returns: TODO

        """
        keys = list(activities.keys())
        print("keys: {}".format(keys))

        for k in keys:
            node = Node(k, activities[k]["duration"])
            self.nodes[k] = node

        for k in keys:
            for d in activities[k]["dependencies"]:
                self.nodes[k].add_dependency(self.nodes[d])
                self.nodes[d].add_successor(self.nodes[k])

    def forward_pass(self):
        completed = []

        while len(completed) != len(self.nodes):
            possible = [
                n for n in self.nodes.values() if
                all(d in completed for d in n.dependencies)
                and
                n not in completed
            ]

            for p in possible:
                p.forward_pass(0)
                completed.append(p)

    def backward_pass(self):
        completed = []

        leaves = [n for n in self.nodes.values() if not n.successors]
        highest_early_finish = max([l.earliest_finish for l in leaves])

        while len(completed) != len(self.nodes):
            possible = [
                n for n in self.nodes.values() if
                all(d in completed for d in n.successors)
                and
                n not in completed
            ]

            for p in possible:
                p.backward_pass(highest_early_finish)
                completed.append(p)

    def calculate_floats(self):
        leaves = [n for n in self.nodes.values() if not n.successors]
        highest_early_finish = max([l.earliest_finish for l in leaves])

        for n in self.nodes.values():
            n.calculate_float(highest_early_finish)
