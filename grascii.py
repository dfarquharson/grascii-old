# Constants
__horizontal__ = '-'
__vertical__ = '|'
__corner__ = '+'
__space__ = ' '
__arrow_left__ = '<'
__arrow_right__ = '>'
__arrow_up__ = '^'
__arrow_down__ = 'v'

# TODO: modes
# - Automatic (does a best-guess placement of nodes and edges)
# - ManualNode (takes specified coordinates for node placement,
#               but still automates edge placement)
# - ManualFull (specified node and edge placement)


def make_node(node_name):
    len_node_name = len(node_name)
    hline = __corner__ + (__horizontal__ * (len_node_name + 2)) + __corner__
    vline = __vertical__ + __space__ + node_name + __space__ + __vertical__
    return '\n'.join([hline, vline, hline])
