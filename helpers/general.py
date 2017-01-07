from copy import deepcopy

from block import Block
from filter import Filter
from properties.color import Color
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


def add_failsafe(_filter: Filter):
    _filter.add(Block(show=False,
                      rarity=Comparer('Magic', '<='),
                      _class=['Bows', 'Wand', 'Sceptre', 'Staves', 'Claws', 'Body Armour', 'Gloves', 'Boots', 'Helmets',
                              'Quivers', 'Flask', 'Daggers', 'Shields', 'Belts', 'Rings', 'Amulets', 'Two Hand Axes',
                              'Two Hand Maces', 'Two Hand Swords', 'One Hand Axes', 'One Hand Maces', 'One Hand Swords',
                              'Thrusting One Hand Swords'],
                      theme=Theme(background_color=Color(0, 0, 0, 165), font_size=20)))
    _filter.add(Block(show=False,
                      _class=['Skill Gems'],
                      theme=Theme(background_color=Color(0, 0, 0, 165), font_size=20)))
    _filter.add(Block(theme=Theme(text_color=Color(255, 0, 255), border_color=Color(255, 0, 255), font_size=45)))
