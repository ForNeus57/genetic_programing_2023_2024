import random
from utils import select_random_node, simplify_expression, read_input_params, read_config

def crossover(tree1, tree2):
    config = read_config("data/config.json")
    max_depth = config["DEPTH"]

    node1, depth1 = select_random_node(tree1, max_depth)
    node2, depth2 = select_random_node(tree2, max_depth)

    if node1 is not None and node2 is not None:
        if depth1 + node2.depth() - 1 <= max_depth and depth2 + node1.depth() - 1 <= max_depth:
            node1.left, node2.left = node2.left, node1.left
            node1.right, node2.right = node2.right, node1.right
            simplify_expression(node1)
            simplify_expression(node2)
    return tree1, tree2
