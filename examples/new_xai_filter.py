from copy import deepcopy

from block import Block
from comment import Comment
from filter import Filter
from helpers.base_types_and_classes import atlas_bases, gg_es_bases, gg_spell_bases, jewellery, good_spell_bases, \
    good_armour_bases, gg_phys_bases, good_phys_bases, gg_atlas_bases, other_atlas_bases, melee_only_classes
from helpers.colors import Colors
from helpers.general import add_failsafe, ilvl_swap, small_sizes
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
                   'Remnant of Corruption', 'Essence of', 'Cartographer\'s Chisel', 'Orb of Alchemy']
    t4_currency = ['Silver Coin', 'Orb of Chance', 'Jeweller\'s Orb', 'Orb of Alteration', 'Chromatic Orb']

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

    show_jewellery = 0
    chromatic_recipe = 2
    flasks = 2

    crude_bow = True

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
    f.add(Block(theme=t['breach_big'], _class=['Stackable Currency'], base_type=['Splinter of Chayula', 'Splinter of Esh']))
    f.add(Block(theme=t['breach'], _class=['Stackable Currency'], base_type=['Splinter']))
    f.add(Block(theme=t['t4_currency'], base_type=t4_currency))
    f.add(Block(_class=['Currency'], base_type=['Wisdom']))
    f.add(Block(_class=['Currency'], base_type=['Portal']))
    f.add(Block(theme=t['t5_currency'], _class=['Currency', 'Stackable Currency']))

    f.add(Comment('Section: #007 - Divination Cards\n'))
    f.add(Block(theme=t['t4_div'], base_type='The Wolf\'s Shadow',
                comment='Added here so that "The Wolf" doesn\'t get confused with "The Wolf\'s Shadow"(Thanks Neversink for this tip!)'))
    f.add(Block(theme=t['t1_div'], base_type=t1_divs))
    f.add(Block(theme=t['t2_div'], base_type=t2_divs))
    f.add(Block(theme=t['t4_div'], base_type=t4_divs))
    f.add(Block(show=False, base_type=shit_divs))
    f.add(Block(theme=t['t3_div'], _class='Divination Card'))

    f.add(Comment('Section: #008 - Socket/Link Stuff\n'))
    f.add(Block(theme=t['five_link'], play_alert_sound=Sound(1), linked_sockets=5))
    f.add(Block(theme=t['six_socket'], sockets=Comparer(6, '>=')))

    f.add(Comment('Section: #009 - Gems\n'))
    f.add(
        Block(theme=t['t1_gems'], _class='Skill Gems', base_type=['Empower', 'Enlighten'], quality=Comparer(10, '>=')))
    f.add(Block(theme=t['t1_gems'], _class='Skill Gems', quality=Comparer(19, '>=')))
    f.add(Block(theme=t['t2_gems'], _class='Skill Gems', base_type=['Portal', 'Empower', 'Enlighten', 'Vaal Haste']))
    f.add(Block(theme=t['t2_gems'], _class='Skill Gems', quality=Comparer(13, '>=')))
    f.add(Block(theme=t['t3_gems'], _class='Skill Gems', base_type=['Vaal', 'Detonate Mines', 'Added Chaos Damage']))
    f.add(Block(theme=t['t3_gems'], _class='Skill Gems', quality=Comparer(1, '>=')))
    f.add(Block(_class='Skill Gems'))

    f.add(Comment('Section: #010 - Rare Evaluation\n'))
    f.add(Block(theme=t['rare_jewel'], _class='Jewel', rarity='Rare'))
    f.add(Block(theme=t['rare_talisman'], base_type=['Talisman'], rarity='Rare'))
    f.add(Block(theme=t['talisman'], base_type=['Talisman'], rarity=Comparer('Rare', '<')))
    f.add(Block(theme=t['ggg_rare'], item_level=Comparer(84, '>='), base_type=atlas_bases, rarity='Rare'))
    f.add(
        Block(theme=t['gg_rare'], item_level=Comparer(84, '>='), rarity='Rare', base_type=gg_es_bases + gg_spell_bases))
    f.add(Block(theme=t['gg_rare'], item_level=Comparer(84, '>='), rarity='Rare', _class=jewellery))
    f.add(Block(theme=t['gg_rare'], item_level=Comparer(84, '>='), rarity='Rare',
                base_type=good_spell_bases + good_armour_bases, set_font_size=38))
    f.add(Block(theme=t['gg_rare'], item_level=Comparer(84, '>='), rarity='Rare', base_type='Sai', _class='Daggers',
                set_font_size=38))
    f.add(Block(theme=t['gg_rare'], item_level=Comparer(83, '>='), rarity='Rare', base_type=gg_phys_bases))
    f.add(Block(theme=t['gg_rare'], item_level=Comparer(83, '>='), rarity='Rare', base_type=good_phys_bases,
                set_font_size=38))
    f.add(Block(theme=t['ggg_rare'], rarity='Rare', base_type=gg_atlas_bases))
    f.add(
        Block(theme=t['ggg_rare'], rarity='Rare', play_alert_sound=None, set_font_size=42, base_type=other_atlas_bases))
    f.add(Block(theme=t['good_rare_ilvl'], rarity='Rare', base_type=good_phys_bases, item_level=Comparer(73, '>=')))
    f.add(Block(theme=t['good_rare_ilvl'], item_level=Comparer(72, '>='), rarity='Rare', base_type='Sai',
                _class='Daggers'))
    f.add(Block(theme=t['good_rare_ilvl'], item_level=Comparer(72, '>='), rarity='Rare',
                base_type=good_armour_bases + gg_es_bases))
    f.add(Block(theme=t['good_rare'], rarity='Rare',
                base_type=good_phys_bases + gg_es_bases + good_armour_bases + gg_spell_bases + good_spell_bases))
    ilvl_swap(f, Block(theme=t['good_rare_ilvl'], item_level=Comparer(75, '>='), rarity='Rare', _class=jewellery,
                       set_font_size=40), t['good_rare'], set_font_size=40)
    ilvl_swap(f, Block(theme=t['good_rare_ilvl'], set_font_size=35, rarity='Rare', item_level=Comparer(73, '>='),
                       drop_level=Comparer(59, '>='), _class=['Wands', 'Daggers', 'Sceptres']), t['good_rare'],
              set_font_size=35)
    f.add(Block(theme=t['shit_rare'], item_level=Comparer(65, '>='), drop_level=Comparer(55, '<='),
                _class=melee_only_classes, rarity='Rare'))
    ilvl_swap(f, Block(theme=t['good_rare_ilvl'], item_level=Comparer(74, '>='), rarity='Rare', _class='Quivers',
                       set_font_size=35,
                       base_type=['Spike-Point Arrow Quiver', 'Broadhead Arrow Quiver', 'Two-Point Arrow Quiver']),
              lower_theme=t['good_rare'], set_font_size=35)
    ilvl_swap(f, Block(theme=t['good_rare_ilvl'], item_level=Comparer(72, '>='), drop_level=Comparer(44, '>='),
                       rarity='Rare', _class=['Gloves', 'Boots', 'Helmets'], set_font_size=35),
              lower_theme=t['good_rare'], set_font_size=35)
    f.add(Block(theme=t['shit_rare'], item_level=Comparer(65, '>='), drop_level=Comparer(15, '<='),
                _class=['Gloves', 'Boots', 'Helmets'],
                rarity='Rare'))
    f.add(Block(theme=t['shit_rare'], item_level=Comparer(65, '>='), drop_level=Comparer(50, '<='), _class='Shields',
                rarity='Rare'))
    f.add(
        Block(theme=t['shit_rare'], item_level=Comparer(65, '>='), drop_level=Comparer(47, '<='), _class='Body Armour',
              rarity='Rare'))
    f.add(Block(theme=t['good_rare'], set_font_size=45, item_level=Comparer(30, '<'), rarity='Rare', _class='Boots'))
    f.add(Block(theme=t['good_rare'], item_level=Comparer(65, '<'), rarity='Rare',
                _class=['Boots', 'Helmets', 'Gloves', 'Sceptres', 'Daggers', 'Wands']))
    f.add(Block(theme=t['good_rare'], item_level=Comparer(10, '<'), rarity='Rare'))
    # nice example of what you can do with PoEFilter
    for drop_level in range(5, 56):
        f.add(Block(theme=t['good_rare'], item_level=Comparer(drop_level + 10, '<'),
                    drop_level=Comparer(drop_level, '>'),
                    rarity='Rare', set_font_size=35))

    f.add(Block(theme=Theme(background_color=Colors.BLACK, border_color=Color(150, 150, 150), font_size=35),
                item_level=Comparer(20, '<'), rarity='Rare'))
    f.add(Block(theme=Theme(background_color=Color(0, 0, 0, 180), border_color=Color(150, 150, 150), font_size=35),
                item_level=Comparer(65, '<'), rarity='Rare'))
    f.add(Block(theme=Theme(background_color=Color(0, 0, 0, 225), border_color=Color(150, 150, 150), font_size=26),
                rarity='Rare', width=Comparer(2, '>='), height=Comparer(4, '>=')))
    small_sizes(f, Block(rarity='Rare',
                         theme=Theme(background_color=Colors.BLACK, border_color=Color(150, 150, 150), font_size=35)))
    f.add(Block(theme=Theme(background_color=Color(0, 0, 0, 180), border_color=Color(150, 150, 150), font_size=35),
                rarity='Rare'))

    f.add(Comment('Section: #011 - Normal and Magic Items\n'))
    # f.add(Block(theme=Theme(background_color=Color(0, 0, 0, 0), border_color=Colors.BLOOD_RED, text_color=Colors.BLOOD_RED), comment='Animate Weapon', rarity='Normal', _class=['One Hand', 'Two Hand', 'Staves', 'Daggers', 'Thrusting', 'Sceptres', 'Claws']))
    f.add(Block(comment='Redblade(potentially)', rarity='Magic', _class='Helmets', identified=True,
                set_border_color=Color(210, 0, 0)))
    f.add(Block(theme=t['gg_atlas_base'], base_type=atlas_bases, item_level=Comparer(84, '>=')))
    f.add(Block(theme=t['gg_white_base'], item_level=Comparer(84, '>='), base_type=gg_es_bases + gg_spell_bases))
    f.add(Block(theme=t['gg_white_base'], item_level=Comparer(84, '>='), _class=jewellery))
    f.add(
        Block(theme=t['ok_white_base'], item_level=Comparer(84, '>='), base_type=good_spell_bases + good_armour_bases))
    f.add(Block(theme=t['ok_white_base'], item_level=Comparer(84, '>='), base_type='Sai', _class='Daggers'))
    f.add(Block(theme=t['gg_white_base'], item_level=Comparer(83, '>='), base_type=gg_phys_bases))
    f.add(Block(theme=t['ok_white_base'], item_level=Comparer(83, '>='), base_type=good_phys_bases))
    f.add(Block(theme=t['gg_atlas_base'], base_type=gg_atlas_bases))
    f.add(Block(theme=t['atlas_base'], base_type=other_atlas_bases))
    if crude_bow:
        f.add(Block(theme=t['gg_white_base'], base_type=['Crude Bow'], item_level=Comparer(50, '>=')))
    if chromatic_recipe >= 1:
        small_sizes(f, Block(theme=t['chromatic_item'], socket_group='RGB'))
    if chromatic_recipe == 2:
        f.add(Block(theme=t['chromatic_item'], set_font_size=30, socket_group='RGB'))
    f.add(Block(theme=t['chance_item'], rarity='Normal',
                base_type=['Sorcerer Boots', 'Occultist\'s Vestment', 'Sapphire Flask',
                           'Spike-Point Arrow Quiver', 'Imperial Staff']))
    if show_jewellery >= 2:
        f.add(Block(theme=t['alch_whites'], item_level=Comparer(67, '>='), rarity='Normal', _class=jewellery,
                    base_type=['Onyx', 'Ruby', 'Sapphire', 'Topaz', 'Two-Stone', 'Diamond', 'Prismatic', 'Unset',
                               'Gold',
                               'Citrine', 'Turquoise', 'Agate', 'Coral Ring', 'Moonstone', 'Leather', 'Heavy', 'Amber',
                               'Jade', 'Lapis', 'Rustic', 'Iron Ring']))
    if show_jewellery >= 1:
        f.add(Block(theme=t['magic_jewellery'], item_level=Comparer(67, '>='), rarity='Magic', _class=jewellery))
    f.add(Block(theme=t['magic_jewel'], _class='Jewel'))
    f.add(Block(item_level=Comparer(75, '>='), base_type=gg_es_bases))

    f.add(Comment('Section: #0012 - Flasks\n'))
    if flasks >= 1:
        f.add(Block(theme=t['high_quality_flask'], quality=Comparer(18, '>='), rarity='Magic', _class='Utility Flasks'))
        f.add(
            Block(theme=t['high_quality_flask'], quality=Comparer(15, '>='), rarity='Normal', _class='Utility Flasks'))
        f.add(
            Block(theme=t['high_quality_flask'], quality=Comparer(1, '>='), _class='Utility Flasks', set_font_size=38))
    f.add(Block(theme=t['utility_flask'], _class='Utility Flasks', item_level=Comparer(10, '<='), set_font_size=38))
    f.add(Block(theme=t['utility_flask'], _class='Utility Flasks', item_level=Comparer(25, '<='), set_font_size=37))
    f.add(Block(theme=t['utility_flask'], _class='Utility Flasks', item_level=Comparer(50, '<='), set_font_size=36))
    if flasks >= 2:
        f.add(Block(theme=t['utility_flask'], _class='Utility Flasks'))
        f.add(Block(_class=['Life Flask', 'Mana Flask'], item_level=Comparer(72, '>='), set_font_size=20))
    hybrid_flask_ilvl_to_keyword = {
        15: 'Small',
        25: 'Medium',
        35: 'Large',
        45: 'Colossal',
        55: 'Sacred',
        67: 'Hallowed',
    }
    for ilvl, base_type in sorted(hybrid_flask_ilvl_to_keyword.items()):
        f.add(Block(set_font_size=38, item_level=Comparer(ilvl, '<='), _class='Hybrid Flask', base_type=base_type))

    normal_flask_ilvl_to_keyword = {
        5: 'Small',
        8: 'Medium',
        12: 'Large',
        18: 'Greater',
        24: 'Grand',
        30: 'Giant',
        37: 'Colossal',
        42: 'Sacred',
        48: 'Hallowed',
        55: 'Sanctified',
        66: ['Divine', 'Eternal'],
    }
    for ilvl, base_type in sorted(normal_flask_ilvl_to_keyword.items()):
        f.add(Block(set_font_size=38, item_level=Comparer(ilvl, '<='), _class='Flask', base_type=base_type))

    if flasks >= 2:
        f.add(Block(rarity=Comparer('Magic', '<='), base_type='Flask', set_font_size=30))

    f.add(Comment('Section: #0013 - Leveling\n'))
    f.add(Block(theme=t['early_survival'], item_level=Comparer(12, '<'),
                base_type=['Coral Ring', 'Sapphire Ring', 'Leather Belt']))
    f.add(Block(theme=t['early_survival'], item_level=Comparer(12, '<'), set_font_size=38,
                base_type=['Padded Vest', 'Light Brigandine', 'Leather Cap', 'Shabby Jerkin', 'Scale Vest',
                           'Rawhide Boots', 'Rawhide Gloves', 'Leatherscale Boots', 'Wrapped Boots', 'Goathide Gloves',
                           'Fishscale Gauntlets', 'Wrapped Mitts', 'Battered Helm', 'Scare Mask', 'Goathide Buckler',
                           'Pine Buckler', 'Rotted Round Shield', 'Spiked Bundle']))
    f.add(Block(item_level=Comparer(35, '<'), rarity='Normal', _class=jewellery))
    f.add(Block(item_level=Comparer(66, '<='), rarity='Magic', _class=jewellery))
    f.add(Block(item_level=Comparer(68, '<'), rarity='Magic', linked_sockets=4, _class='Boots', theme=Theme(
            border_color=Color(255, 255, 255), font_size=38
    )))
    f.add(Block(item_level=Comparer(25, '<'), rarity='Magic', set_font_size=38, _class='Boots'))
    f.add(Block(item_level=Comparer(35, '<'), rarity=Comparer('Magic', '<='), linked_sockets=3,
                _class=['Sceptres', 'Wands', 'Daggers'],
                theme=Theme(border_color=Color(255, 255, 255), font_size=36)))
    f.add(Block(item_level=Comparer(25, '<'), rarity=Comparer('Magic', '<='), _class=['Sceptres', 'Wands', 'Daggers'],
                set_font_size=36))
    f.add(Block(item_level=Comparer(66, '<='), linked_sockets=Comparer(4, '>='),
                theme=Theme(border_color=Color(255, 255, 255), font_size=36)))
    f.add(Block(item_level=Comparer(25, '<='), linked_sockets=Comparer(3, '>='), _class=['Gloves', 'Boots', 'Helmets'],
                set_font_size=36))
    f.add(Block(item_level=Comparer(60, '<='), linked_sockets=Comparer(3, '>='), _class=['Gloves', 'Boots', 'Helmets']))
    f.add(Block(item_level=Comparer(12, '<'), linked_sockets=Comparer(3, '>='),
                theme=Theme(font_size=36, background_color=Color(0, 0, 0, 185))))
    f.add(Block(item_level=Comparer(12, '<'), rarity='Normal', width=2, height=Comparer(3, '>='),
                _class=['Body Armours', 'Shields'],
                theme=Theme(text_color=Color(200, 200, 200, 180), background_color=Color(0, 0, 0, 165))))
    f.add(Block(item_level=Comparer(12, '<'), rarity='Normal', width=2, height=Comparer(4, '>='),
                theme=Theme(text_color=Color(200, 200, 200, 180), background_color=Color(0, 0, 0, 165))))
    small_sizes(f, Block(item_level=Comparer(12, '<='), rarity='Normal',
                         theme=Theme(text_color=Color(200, 200, 200), background_color=Color(0, 0, 0, 185))))
    f.add(Block(item_level=Comparer(12, '<'), rarity='Normal',
                theme=Theme(font_size=32, background_color=Color(0, 0, 0, 165))))
    leveling_weapon_classes = ['Two Hand', 'Bows', 'One Hand', 'Wand', 'Sceptre', 'Staves', 'Claws']
    item_and_drop_levels = [(13, 8), (14, 9), (16, 11), (18, 14), (20, 17), (22, 19), (24, 21), (26, 24), (28, 26),
                            (30, 28), (32, 30), (34, 32), (36, 34), (38, 37), (40, 39), (42, 41), (48, 46), (50, 48),
                            (52, 50), (54, 52), (56, 54), (58, 56), (62, 60), (66, 65), (68, 67)]
    for i_and_d in item_and_drop_levels:
        f.add(Block(item_level=Comparer(i_and_d[0], '<'), drop_level=Comparer(i_and_d[1], '>='),
                    rarity=Comparer('Magic', '<='),
                    _class=leveling_weapon_classes, theme=Theme(font_size=32, background_color=Color(0, 0, 0, 165))))
    f.add(Block(item_level=Comparer(12, '<'), rarity='Magic', width=2, height=Comparer(3, '>='),
                _class=['Body Armours', 'Shields'],
                theme=Theme(text_color=Color(156, 156, 235, 150), background_color=Color(0, 0, 0, 165))))
    f.add(Block(item_level=Comparer(12, '<'), rarity='Magic', width=2, height=Comparer(4, '>='),
                theme=Theme(text_color=Color(156, 156, 235, 150), background_color=Color(0, 0, 0, 165))))
    small_sizes(f, Block(item_level=Comparer(12, '<='), rarity='Magic',
                         theme=Theme(background_color=Color(0, 0, 0, 185))))
    f.add(Block(item_level=Comparer(24, '<'), rarity='Magic',
                theme=Theme(font_size=32, background_color=Color(0, 0, 0, 165))))
    f.add(Block(item_level=Comparer(36, '<'), rarity='Magic',
                theme=Theme(font_size=26, background_color=Color(0, 0, 0, 165))))

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

    good_rare = Color(198, 186, 9).darken(0.1)
    rare = good_rare.darken(0.2)

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
        't3_unique': Theme(text_color=Colors.BLACK, border_color=highlight_1, background_color=Colors.UNIQUE,
                           alert_sound=3, font_size=40),
        't4_unique': Theme(text_color=break_1, border_color=break_1, background_color=Colors.UNIQUE,
                           font_size=35),
        'low_map': Theme(background_color=break_2.change_opacity(122), text_color=Colors.BLACK,
                         border_color=Colors.BLACK, font_size=35),
        'normal_map': Theme(background_color=break_2, text_color=Colors.BLACK, border_color=Colors.BLACK,
                            alert_sound=2, font_size=40),
        'good_map': Theme(background_color=break_2, text_color=highlight_1, border_color=highlight_1,
                          alert_sound=9, font_size=45),
        't2_fragment': Theme(text_color=Colors.BLACK, background_color=Colors.BLOOD_RED, border_color=Colors.BLACK,
                             font_size=45, alert_sound=2),
        't3_fragment': Theme(text_color=Colors.BLOOD_RED, background_color=Colors.BLACK, border_color=Colors.BLOOD_RED,
                             font_size=38, alert_sound=2),
        't2_currency': Theme(background_color=highlight_2, text_color=break_3, border_color=break_3, alert_sound=5,
                             font_size=45),
        't3_currency': Theme(background_color=break_3, text_color=Colors.WHITE, border_color=Colors.WHITE,
                             alert_sound=1, font_size=41),
        't4_currency': Theme(background_color=highlight_1, text_color=Colors.WHITE, border_color=Colors.WHITE,
                             font_size=38),
        't5_currency': Theme(background_color=highlight_1.change_opacity(0.5), text_color=Colors.WHITE,
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
        't3_gems': Theme(text_color=gem_colour, border_color=gem_colour, font_size=37),

        'five_link': Theme(background_color=highlight_1, border_color=Colors.WHITE, font_size=38, alert_sound=1),
        'six_socket': Theme(background_color=break_3, border_color=Colors.WHITE, alert_sound=7, font_size=45),

        'leaguestone': Theme(background_color=highlight_2.darken(0.3), text_color=Colors.WHITE,
                             border_color=Colors.WHITE,
                             alert_sound=4, font_size=38),
        'breach': Theme(background_color=breach, text_color=Colors.BLOOD_RED, border_color=Colors.BLOOD_RED),
        'breach_big': Theme(background_color=breach, text_color=Colors.BLOOD_RED, border_color=Colors.BLOOD_RED, font_size=40),

        'rare_jewel': Theme(background_color=good_rare, text_color=Colors.WHITE, border_color=Colors.WHITE,
                            font_size=45),
        'ggg_rare': Theme(background_color=good_rare, text_color=break_3, border_color=break_3, font_size=45,
                          alert_sound=5),
        'gg_rare': Theme(background_color=good_rare, text_color=Colors.WHITE, border_color=break_3, font_size=45),
        'good_rare': Theme(background_color=good_rare, text_color=Colors.WHITE, border_color=Colors.BLACK,
                           font_size=40),
        'good_rare_ilvl': Theme(background_color=good_rare, text_color=Colors.WHITE, border_color=break_3,
                                font_size=42),
        'shit_rare': Theme(text_color=rare, border_color=Colors.BLOOD_RED, font_size=30),
        'rare_talisman': Theme(background_color=good_rare, text_color=Colors.BLOOD_RED, border_color=Colors.BLOOD_RED,
                               font_size=45, alert_sound=1),
        'talisman': Theme(border_color=Colors.BLOOD_RED, font_size=38),

        'gg_atlas_base': Theme(background_color=Colors.WHITE, text_color=break_3, border_color=break_3, font_size=45,
                               alert_sound=5),
        'atlas_base': Theme(background_color=Colors.WHITE, text_color=break_3, border_color=break_3, font_size=40),
        'gg_white_base': Theme(font_size=45, border_color=break_3),
        'ok_white_base': Theme(font_size=40, border_color=highlight_1),
        'chromatic_item': Theme(border_color=break_2, background_color=Colors.BLACK.change_opacity(0.5)),
        'chance_item': Theme(border_color=gem_colour, font_size=40),

        'alch_whites': Theme(border_color=rare),
        'magic_jewel': Theme(border_color=break_3, background_color=highlight_1.change_opacity(0.5)),
        'magic_jewellery': Theme(font_size=25),
        'high_quality_flask': Theme(background_color=Color(75, 75, 75), border_color=Colors.WHITE, font_size=45),
        'utility_flask': Theme(background_color=Color(75, 75, 75), border_color=Colors.BLACK),
        'early_survival': Theme(border_color=Colors.BLOOD_RED, font_size=40)

    }


if __name__ == '__main__':
    main()
