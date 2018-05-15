# Constants
horizontal = '-'
vertical = '|'
corner = '+'
space = ' '
arrow_left = '<'
arrow_right = '>'
arrow_up = '^'
arrow_down = 'v'

# TODO: modes
# - Automatic (does a best-guess placement of nodes and edges)
# - ManualNode (takes specified coordinates for node placement,
#               but still automates edge placement)
# - ManualFull (specified node and edge placement)


def make_node(node_name):
    hline = corner + (horizontal * (len(node_name) + 2)) + corner
    vline = vertical + space + node_name + space + vertical
    return '\n'.join([hline, vline, hline])
