from copy import deepcopy

from block import Block
from filter import Filter
from properties.comparer import Comparer
from theme import Theme


def ilvl_swap(_filter: Filter, block: Block, lower_theme: Theme, **kwargs):
    _filter.add(block)
    other_block = deepcopy(block)
    other_block.set_property('item_level', None)
    other_block.set_theme(lower_theme)
    for key, value in kwargs.items():
        other_block.set_property(key, value)
    _filter.add(other_block)


def small_sizes(_filter: Filter, block: Block):
    block.set_property('width', Comparer(2, '<='))
    block.set_property('height', Comparer(2, '<='))
    _filter.add(block)
    other_block = deepcopy(block)
    other_block.set_property('width', Comparer(1, '<='))
    other_block.set_property('height', Comparer(3, '<='))
    _filter.add(other_block)
