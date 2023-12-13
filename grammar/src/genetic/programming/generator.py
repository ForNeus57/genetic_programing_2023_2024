from tree import Node
from src.utils import simplify_expression
import random


def random_operator():
    return random.choice(['+', '-', '*', '/'])


def random_operand(minrand, maxrand):
    return random.uniform(minrand, maxrand)


def create_random_node(max_depth, minrand, maxrand, depth=0):
    if depth >= max_depth:
        return Node(random_operand(minrand, maxrand))
    operator = random_operator()
    left = create_random_node(max_depth, minrand, maxrand, depth + 1)
    right = create_random_node(max_depth, minrand, maxrand, depth + 1)
    return Node(operator, left, right)


def generate_random_tree(max_depth, minrand, maxrand):
    tree = create_random_node(max_depth, minrand, maxrand)
    simplify_expression(tree)
    return tree
