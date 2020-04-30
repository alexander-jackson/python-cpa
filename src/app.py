import json

from graph import Graph

def process_path(path: str):
    """Performs CPA for a given filepath

    Args:
        path: The filepath to perform CPA on

    """
    with open(path, "r") as f:
        activities = json.load(f)

    graph = Graph(activities)

    graph.forward_pass()
    graph.backward_pass()
    graph.calculate_floats()
    graph.display_calculated_values()
