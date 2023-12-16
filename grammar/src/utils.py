import json
import random


def read_input_params(file_path):
    with open(file_path, 'r') as f:
        params = f.readline().split()
        param_names = ["nvar", "nrand", "minrand", "maxrand", "fitcases"]
        param_values = map(int, params)
        return dict(zip(param_names, param_values))


def read_input_data(file_path, nvar):
    with open(file_path, 'r') as f:
        f.readline()
        data = []
        for line in f:
            data.append(list(map(float, line.split())))
        return data


def read_config(file_path):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config


# idk if this is obligatory but looks better
def simplify_expression(node):
    if node.left and node.right:
        right_value = str(node.right.value)
        if node.value == '+' and right_value.startswith('-'):
            node.value = '-'
            node.right.value = right_value[1:]
        elif node.value == '-' and right_value.startswith('-'):
            node.value = '+'
            node.right.value = right_value[1:]
        simplify_expression(node.left)
        simplify_expression(node.right)


def select_random_node(tree, max_depth, depth=0):
    if depth >= max_depth or not tree:
        return None, depth
    if (not tree.left and not tree.right) or random.randint(0, 1) == 0:
        return tree, depth
    if random.randint(0, 1) == 0:
        return select_random_node(tree.left, max_depth, depth + 1)
    return select_random_node(tree.right, max_depth, depth + 1)
