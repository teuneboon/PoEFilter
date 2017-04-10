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

    t1_currency = ['Exalted Orb', 'Eternal Orb', 'Albino Rhoa Feather', 'Ancient Reliquary Key']
    t2_currency = ['Deafening Essence', 'Shrieking Essence', 'Divine Orb', 'Unshaping Orb', 'Essence of Hysteria',
                   'Essence of Insanity', 'Essence of Horror', 'Essence of Delirium', 'Blessing']
    t3_currency = ['Cartographer\'s Sextant', 'Chaos Orb', 'Cartographer\'s Seal', 'Orb of Fusing', 'Orb of Regret',
                   'Regal Orb', 'Blessed Orb', 'Gemcutter\'s Prism', 'Orb of Scouring', 'Vaal Orb',
                   'Remnant of Corruption', 'Essence of']
    t4_currency = ['Orb of Alchemy', 'Silver Coin', 'Orb of Chance', 'Jeweller\'s Orb', 'Orb of Alteration',
                   'Cartographer\'s Chisel']

    t1_divs = ['House of Mirrors', 'The Doctor', 'The Fiend', 'Hunter\'s Reward', 'The Dragon\'s Heart', 'Mawr Blaidd',
               'The Last One Standing', 'The Offering', 'The Ethereal', 'The Queen', 'Abandoned Wealth',
               'The Brittle Emperor', 'The Immortal', 'The Artist', 'Wealth and Power', 'Pride Before the Fall',
               'The Enlightened', 'The King\'s Heart', 'Bowyer\'s Dream', 'The Hunger', 'The Celestial Justicar',
               'Spark and the Flame', 'Polymath']
    t2_divs = ['Chaotic Disposition', 'The Void', 'The Cartographer', 'The Dapper Prodigy', 'The Vast', 'The Dark Mage',
               'Last Hope', 'The Valkyrie', 'The Sephirot', 'The Hoarder', 'The Chains that Bind', 'The Warlord',
               'The Aesthete', 'Saint\'s Treasure', 'The Thaumaturgist', 'Heterochromia', 'The Porcupine',
               'The Stormcaller', 'The Soul', 'Emperor of Purity', 'The Road to Power', 'The Arena Champion',
               'The Gladiator', 'Glimmer of Hope', 'The Tyrant', 'The Union', 'The Risk', 'The Trial',
               'Scholar of the Seas', 'Lucky Deck', 'Humility', 'The Penitent', 'The Penitent', 'The Surveyor',
               'Lysah\'s Respite', 'The Inventor', 'The Jester', 'Vinia\'s Token', 'Rats', 'The Wrath', 'Hope',
               'Treasure Hunter', 'The Explorer', 'The Body', 'Jack in the Box', 'The Traitor', 'Valley of Steel Boxes',
               'Wolven King\'s Bite', 'Wretched', 'The Opulent', 'Might is Right', 'The Fletcher', 'The Forsaken',
               'The Formless Sea', 'The Demoness', 'Time-Lost Relic', 'The Wolf', 'Earth Drinker', 'Standoff',
               'Merciless Armament']
    t4_divs = ['The Flora\'s Gift', 'Her Mask', 'Rain of Chaos', 'Thunderous Skies', 'The Gambler']
    shit_divs = ['The Carrion Crow', 'Doedre\'s Madness']

    f = Filter()
    t = themes()

    f.add(Comment('Section: #001 - Special Stuff\n'))
    f.add(Block(theme=t['t2_unique'],
                comment='Tabula, we have to put this before everything cause our 6L block will override otherwise',
                socket_group='W' * 6,
                rarity='Unique',
                base_type='Simple Robe'))
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
    f.add(Block(theme=t['t1_unique'], rarity='Unique', base_type=t1_uniques, comment='T1 Uniques'))
    f.add(Block(theme=t['t2_unique'], rarity='Unique', _class=['Map'], comment='T2 Unique Maps'))
    f.add(Block(theme=t['t2_unique'], rarity='Unique', base_type=t2_uniques, comment='T2 Uniques'))
    f.add(Block(theme=t['t4_unique'], rarity='Unique', base_type=t4_uniques, sockets=Comparer(6, '<'),
                linked_sockets=Comparer(5, '<'), comment='T4 Uniques'))
    f.add(Block(theme=t['t3_unique'], rarity='Unique', comment='Other(T3) Uniques'))

    f.add(Comment('Section: #004 - Maps\n'))
    maps = get_maps_by_drop_level()
    f.add(Block(theme=t['good_map'], _class='Maps', base_type='Shaped',
                drop_level=Comparer(shaped_maps_special_tier + 67, '>=')))
    f.add(Block(theme=t['good_map'], _class='Maps', base_type=special_maps, comment='Special Maps(usually MF)'))
    for drop_level in list(maps.keys())[::-1]:
        if drop_level == 68:
            drop_level = 58
        base_block = Block(_class='Maps', drop_level=Comparer(drop_level, '>='),
                           item_level=Comparer(drop_level - map_no_sound_tier_difference, '>='))
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

    f.add(Comment('Section: #005 - Fragments\n'))
    f.add(Block(play_alert_sound=Sound(2), _class='Maps'))  # map failsafe
    f.add(Block(theme=t['t1'], _class='Map Fragments',
                base_type=['Mortal Hope', 'Mortal Ignorance', 'Fragment of the Phoenix',
                           'Fragment of the Minotaur', 'Fragment of the Chimera', 'Fragment of the Hydra']))
    f.add(Block(theme=t['t2_fragment'], _class='Map Fragments',
                base_type=['Mortal', 'Sacrifice at Midnight', 'Eber\'s Key', 'Inya\'s Key', 'Volkuur\'s Key',
                           'Yriel\'s Key', 'Breachstone']))
    f.add(Block(theme=t['t3_fragment'], _class='Map Fragments'))

    f.add(Comment('Section: #006 - Currency + Essences + Leaguestones\n'))
    f.add(Block(theme=t['t1'], base_type=t1_currency))
    f.add(Block(theme=t['t2_currency'], base_type=t2_currency))
    f.add(Block(theme=t['leaguestone'], _class='Leaguestone'))
    f.add(Block(theme=t['t3_currency'], base_type=t3_currency))
    f.add(Block(theme=Theme(text_color=Color(231, 180, 120),
                            background_color=Color(0, 0, 0, 180),
                            border_color=Color(231, 180, 120),
                            font_size=45),
                base_type='Perandus Coin'))
    f.add(Block(theme=t['breach'], _class=['Stackable Currency'], base_type=['Splinter']))
    f.add(Block(theme=t['t4_currency'], base_type=t4_currency))
    f.add(Block(_class=['Currency'], base_type=['Wisdom']))
    f.add(Block(_class=['Currency'], base_type=['Portal']))
    f.add(Block(theme=t['t5_currency'], _class=['Currency', 'Stackable Currency']))

    f.add(Comment('Section: #0007 - Divination Cards\n'))
    f.add(Block(theme=t['t4_div'], base_type='The Wolf\'s Shadow',
                comment='Added here so that "The Wolf" doesn\'t get confused with "The Wolf\'s Shadow"(Thanks Neversink for this tip!)'))
    f.add(Block(theme=t['t1_div'], base_type=t1_divs))
    f.add(Block(theme=t['t2_div'], base_type=t2_divs))
    f.add(Block(theme=t['t4_div'], base_type=t4_divs))
    f.add(Block(show=False, base_type=shit_divs))
    f.add(Block(theme=t['t3_div'], _class='Divination Card'))

    f.add(Comment('Section: #0008 - Socket/Link Stuff\n'))
    f.add(Block(theme=t['five_link'], play_alert_sound=Sound(1), linked_sockets=5))
    f.add(Block(theme=t['six_socket'], sockets=Comparer(6, '>=')))

    f.add(Comment('Section: #0009 - Gems\n'))
    f.add(Block(theme=t['t1_gems'], _class='Skill Gems', base_type=['Empower', 'Enlighten'], quality=Comparer(10, '>=')))
    f.add(Block(theme=t['t1_gems'], _class='Skill Gems', quality=Comparer(19, '>=')))
    f.add(Block(theme=t['t2_gems'], _class='Skill Gems', base_type=['Portal', 'Empower', 'Enlighten', 'Vaal Haste']))
    f.add(Block(theme=t['t2_gems'], _class='Skill Gems', quality=Comparer(13, '>=')))
    f.add(Block(theme=t['t3_gems'], _class='Skill Gems', base_type=['Vaal', 'Detonate Mines', 'Added Chaos Damage']))
    f.add(Block(theme=t['t3_gems'], _class='Skill Gems', quality=Comparer(1, '>=')))
    f.add(Block(_class='Skill Gems'))

    f.add(Comment('Section: #014 - Failsafe\n'))
    add_failsafe(f)

    with open('Xai.filter', encoding='utf-8', mode='w') as file:
        file.write(str(f))


def themes():
    t1_highlight = Colors.BLOOD_RED
    t1_background = Colors.WHITE

    highlight_1 = Color(0, 93, 255)
    highlight_2 = Color(53, 255, 177)
    break_1 = Color(255, 230, 122)
    break_2 = Color(122, 255, 148)
    break_3 = Color(0, 52, 112)
    breach = Color(65, 20, 80)

    gem_colour = highlight_2.darken(0.4)

    return {
        'lab_and_shaper_orb': Theme(text_color=highlight_1, background_color=break_1, border_color=highlight_1,
                                    font_size=45, alert_sound=1),
        'quest': Theme(text_color=break_2, border_color=break_2, font_size=45, alert_sound=1),
        't1': Theme(text_color=t1_highlight, border_color=t1_highlight, background_color=t1_background, font_size=45,
                    alert_sound=8),
        't1_unique': Theme(text_color=t1_highlight, border_color=t1_highlight, background_color=t1_background,
                           font_size=45,
                           alert_sound=6),
        't2_unique': Theme(text_color=Colors.WHITE, border_color=Colors.WHITE, background_color=Colors.UNIQUE,
                           alert_sound=5, font_size=45),
        't3_unique': Theme(text_color=highlight_1, border_color=highlight_1, background_color=Colors.UNIQUE,
                           alert_sound=3, font_size=40),
        't4_unique': Theme(text_color=break_1, border_color=break_1, background_color=Colors.UNIQUE,
                           font_size=35),
        'low_map': Theme(background_color=highlight_1.change_opacity(122), text_color=Colors.WHITE,
                         border_color=Colors.WHITE, font_size=35),
        'normal_map': Theme(background_color=highlight_1, text_color=Colors.WHITE, border_color=Colors.WHITE,
                            alert_sound=2, font_size=40),
        'good_map': Theme(background_color=break_2, text_color=Colors.BLACK, border_color=Colors.BLACK,
                          alert_sound=9, font_size=45),
        't2_fragment': Theme(text_color=Colors.BLACK, background_color=Colors.BLOOD_RED, border_color=Colors.BLACK,
                             font_size=45, alert_sound=2),
        't3_fragment': Theme(text_color=Colors.BLOOD_RED, background_color=Colors.BLACK, border_color=Colors.BLOOD_RED,
                             font_size=38, alert_sound=2),
        't2_currency': Theme(background_color=highlight_2, text_color=break_3, border_color=break_3, alert_sound=5,
                             font_size=45),
        't3_currency': Theme(background_color=break_3, text_color=Colors.WHITE, border_color=Colors.WHITE,
                             alert_sound=1, font_size=41),
        't4_currency': Theme(background_color=highlight_1.change_opacity(0.5), text_color=Colors.WHITE,
                             border_color=Colors.WHITE, font_size=38),
        't5_currency': Theme(background_color=highlight_1.change_opacity(0.5), text_color=break_2,
                             border_color=break_2),

        't1_div': Theme(text_color=t1_highlight, border_color=highlight_1, background_color=t1_background, font_size=45,
                        alert_sound=6),
        't2_div': Theme(text_color=break_3, border_color=break_3, background_color=Colors.WHITE, font_size=45,
                        alert_sound=2),
        't3_div': Theme(text_color=highlight_1, border_color=highlight_1, background_color=Colors.WHITE, font_size=40,
                        alert_sound=2),
        't4_div': Theme(text_color=highlight_1, border_color=highlight_1,
                        background_color=Colors.WHITE.change_opacity(0.5)),

        't1_gems': Theme(text_color=break_3, border_color=break_3, background_color=t1_background, font_size=45,
                         alert_sound=6),
        't2_gems': Theme(text_color=break_3, border_color=break_3, background_color=Colors.WHITE, font_size=42,
                         alert_sound=1),
        't3_gems': Theme(text_color=gem_colour, border_color=gem_colour, background_color=Colors.WHITE, font_size=37),

        'five_link': Theme(background_color=highlight_1, border_color=Colors.WHITE, font_size=38, alert_sound=1),
        'six_socket': Theme(background_color=break_3, border_color=Colors.WHITE, alert_sound=7, font_size=45),

        'leaguestone': Theme(background_color=highlight_2.darken(0.3), text_color=Colors.WHITE, border_color=Colors.WHITE,
                             alert_sound=1, font_size=38),
        'breach': Theme(background_color=breach, text_color=Colors.BLOOD_RED, border_color=Colors.BLOOD_RED)
    }


if __name__ == '__main__':
    main()
