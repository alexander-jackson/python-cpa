import json

from graph import Graph

def process_path(path: str):
    """Performs CPA for a given filepath

    Args:
        path: The filepath to perform CPA on

    Returns: TODO

    """
    with open(path, "r") as f:
        contents = json.load(f)

    activities = contents["activities"]
    graph = Graph(activities)

    graph.forward_pass()
    graph.backward_pass()
