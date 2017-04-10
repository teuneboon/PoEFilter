from copy import deepcopy

from block import Block
from comment import Comment
from filter import Filter
from helpers.colors import Colors
from helpers.general import add_failsafe
from helpers.map import get_maps_by_drop_level
from properties.color import Color
from properties.comparer import Comparer
from properties.sound import Sound
from theme import Theme


def main():
    t1_uniques = ['Stibnite Flask', 'Ruby Flask', 'Topaz Flask', 'Sapphire Flask', 'Silver Flask', 'Void Axe',
                  'Prophecy Wand', 'Jewelled Foil', 'Royal Axe', 'Cutlass', 'Sorcerer Boots', 'Occultist\'s Vestment',
                  'Crusader Boots', 'Rawhide Boots', 'Ezomyte Tower Shield', 'Deicide Mask', 'Glorious Plate',
                  'Ezomyte Burgonet', 'Assassin\'s Garb', 'Greatwolf Talisman']
    t2_uniques = ['Granite Flask', 'Bismuth Flask', 'Fiend Dagger', 'Imperial Staff', 'Carnal Sceptre', 'Siege Axe',
                  'Abyssal Axe', 'Sacrificial Garb', 'Ritual Sceptre', 'Judgement Staff', 'Vaal Sceptre',
                  'Imperial Maul', 'Steelhead', 'Carnal Sceptre', 'Terror Maul', 'Jingling Spirit Shield',
                  'Savant\'s Robe', 'Gladiator Plate', 'Vaal Regalia', 'Sacrificial Garb', 'Archon Kite Shield',
                  'Legion Gloves', 'Raven Mask', 'Champion Kite Shield', 'Nightmare Bascinet', 'Clasped Mitts',
                  'Wyrmscale Doublet', 'Gold Ring', 'Crystal Belt', 'Citrine Amulet', 'Ebony Tower Shield',
                  'Onyx Amulet', 'Goathide Boots', 'Two-Stone Ring']
    t4_uniques = ['Plank Kite Shield']

    map_no_sound_tier_difference = 5
    special_maps = ['Beach']
    shaped_maps_special_tier = 10

    f = Filter()
    t = themes()

    f.add(Comment('Section: #001 - Special Stuff\n'))
    f.add(Block(theme=t['lab_and_shaper_orb'], _class='Quest Items', base_type='Shaper\'s Orb'))
    f.add(Block(theme=t['lab_and_shaper_orb'], base_type='Offering to the Goddess'))
    f.add(Block(theme=t['quest'], _class=['Quest Items', 'Microtransactions', 'Hideout Doodads']))
    f.add(Block(theme=t['quest'], _class='Labyrinth', play_alert_sound=Sound(1)))
    f.add(Block(theme=t['t1'], item_level=1, rarity='Normal',
                base_type=['Glass Shank', 'Driftwood Wand', 'Rusted Sword', 'Crude Bow', 'Driftwood Sceptre'],
                play_alert_sound=None,
                comment='Make ilvl 1 of starter weapons ugly so people know they forgot their racing filter @TODO: add others'))

    f.add(Comment('Section: #002 - GG!!!\n'))
    f.add(Block(theme=t['t1'], base_type=['Mirror of Kalandra', 'Fishing Rod']))
    f.add(Block(theme=t['t1'], linked_sockets=Comparer(6, '>=')))

    f.add(Comment('Section: #003 - Uniques\n'))
    f.add(Block(theme=t['t1'], rarity='Unique', base_type=t1_uniques))
    f.add(Block(theme=t['t2_unique'], rarity='Unique', _class=['Map']))
    f.add(Block(theme=t['t2_unique'], rarity='Unique', base_type=t2_uniques))
    f.add(Block(theme=t['t4_unique'], rarity='Unique', base_type=t4_uniques, sockets=Comparer(6, '<'), linked_sockets=Comparer(5, '<')))
    f.add(Block(theme=t['t3_unique'], rarity='Unique'))

    f.add(Comment('Section: #004 - Maps\n'))
    maps = get_maps_by_drop_level()
    f.add(Block(theme=t['good_map'], _class='Maps', base_type='Shaped', drop_level=Comparer(shaped_maps_special_tier + 67, '>=')))
    f.add(Block(theme=t['good_map'], _class='Maps', base_type=special_maps))
    for drop_level in list(maps.keys())[::-1]:
        if drop_level == 68:
            drop_level = 58
        base_block = Block(_class='Maps', drop_level=Comparer(drop_level, '>='), item_level=Comparer(drop_level - map_no_sound_tier_difference, '>='))
        if drop_level >= 82:
            base_block.set_theme(t['good_map'])
        else:
            base_block.set_theme(t['normal_map'])
            if drop_level <= 68:
                base_block.set_property('play_alert_sound', None)
        f.add(base_block)
        no_requirement = deepcopy(base_block)
        no_requirement.set_theme(t['low_map'])
        no_requirement.set_property('item_level', None)
        f.add(no_requirement)


    f.add(Comment('Section: #014 - Failsafe\n'))
    add_failsafe(f)

    with open('Xai.filter', encoding='utf-8', mode='w') as file:
        file.write(str(f))


def themes():
    t1_highlight = Colors.BLOOD_RED
    t1_background = Colors.WHITE

    highlight_1 = Color(0, 93, 255)
    break_1 = Color(255, 230, 122)
    break_2 = Color(122, 255, 148)
    breach = Color(65, 20, 80)

    return {
        'lab_and_shaper_orb': Theme(text_color=highlight_1, background_color=break_1, border_color=highlight_1,
                                    font_size=45, alert_sound=1),
        'quest': Theme(text_color=break_2, border_color=break_2, font_size=45, alert_sound=1),
        't1': Theme(text_color=t1_highlight, border_color=t1_highlight, background_color=t1_background, font_size=45,
                    alert_sound=8),
        't2_unique': Theme(text_color=Colors.WHITE, border_color=Colors.WHITE, background_color=Colors.UNIQUE,
                           alert_sound=5, font_size=45),
        't3_unique': Theme(text_color=highlight_1, border_color=highlight_1, background_color=Colors.UNIQUE,
                           alert_sound=3, font_size=40),
        't4_unique': Theme(text_color=break_1, border_color=break_1, background_color=Colors.UNIQUE,
                           font_size=35),
        'low_map': Theme(background_color=highlight_1.change_opacity(122), text_color=Colors.WHITE, border_color=Colors.WHITE, font_size=35),
        'normal_map': Theme(background_color=highlight_1, text_color=Colors.WHITE, border_color=Colors.WHITE,
                            alert_sound=2, font_size=40),
        'good_map': Theme(background_color=break_2, text_color=Colors.BLACK, border_color=Colors.BLACK,
                          alert_sound=9, font_size=45),
    }


if __name__ == '__main__':
    main()
