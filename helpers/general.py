from copy import deepcopy

from block import Block
from filter import Filter
from theme import Theme


def ilvl_swap(_filter: Filter, block: Block, lower_theme: Theme, **kwargs):
    _filter.add(block)
    other_block = deepcopy(block)
    other_block.set_property('item_level', None)
    other_block.set_theme(lower_theme)
    for key, value in kwargs.items():
        other_block.set_property(key, value)
    _filter.add(other_block)
