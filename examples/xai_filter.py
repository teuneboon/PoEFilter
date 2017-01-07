#!/usr/bin/env python

from colorsys import hsv_to_rgb

from block import Block
from comment import Comment
from filter import Filter
from helpers.base_types_and_classes import atlas_bases, gg_es_bases, gg_spell_bases, jewellery, good_armour_bases, \
    good_spell_bases, \
    gg_phys_bases, good_phys_bases, gg_atlas_bases, other_atlas_bases, melee_only_classes
from helpers.colors import Colors
from helpers.general import ilvl_swap, small_sizes, add_failsafe
from helpers.map import get_all_maps
from properties.color import Color
from properties.comparer import Comparer
from properties.sound import Sound
from theme import Theme


def generate_xai_filter(config=None):
    f = Filter()
    if config is None:
        config = {}
    animate_weapon = config.get('animate_weapon', 'off') == 'on'

    # please don't shoot me for this code
    alch_base, chance_item, chromatic_item, currency, decent_currency, decent_unique, div_cards, early_survival, \
    fragment, gg, gg_div_cards, gg_fragment, gg_gems, good_currency, good_div_cards, good_fragment, good_gems, \
    good_unique, high_quality_flask, magic_jewel, magic_jewellery, meh_div_cards, ok_quality_gems, \
    quality_gems, quest_item, rare_atlas_bases, rare_decent_ilvl_bases, rare_good_bases, rare_jewels, rare_max_ilvl_bases, \
    rare_shit_bases, shaper_maps, shit_currency, shit_div_cards, shit_unique, six_socket, six_socket_special, special_quest_item, \
    unique, utility_flask, white_atlas_bases, white_gg_bases, white_ok_bases, map_theme = get_themes()

    f.add(Comment('Section: #0001 - Special Stuff\n'))
    f.add(Block(theme=decent_unique,
                comment='Tabula, we have to put this before everything cause our 6L block will override otherwise',
                socket_group='W' * 6,
                rarity='Unique',
                base_type='Simple Robe'))
    f.add(Block(theme=special_quest_item, _class='Quest Items', base_type='Shaper\'s Orb'))
    f.add(Block(theme=quest_item, _class=['Quest Items', 'Microtransactions']))
    # @TODO: Add more base types
    f.add(Block(theme=gg, item_level=1, rarity='Normal',
                base_type=['Glass Shank', 'Driftwood Wand', 'Rusted Sword', 'Crude Bow', 'Driftwood Sceptre'],
                play_alert_sound=None,
                comment='Make ilvl 1 of starter weapons ugly so people know they forgot their racing filter @TODO: add others'))

    f.add(Comment('Section: #0002 - Labyrinth\n'))
    f.add(Block(theme=special_quest_item, base_type='Offering to the Goddess'))
    f.add(Block(theme=quest_item, _class='Labyrinth', play_alert_sound=Sound(1)))

    f.add(Comment('Section: #0003 - GG!!!\n'))
    f.add(Block(theme=gg, base_type=['Mirror of Kalandra', 'Fishing Rod']))
    f.add(Block(theme=gg, linked_sockets=Comparer(6, '>=')))

    f.add(Comment('Section: #0004 - Uniques\n'))
    f.add(Block(theme=good_unique, item_level=84, rarity='Unique', base_type=['Infernal Sword', 'Ruby Flask'],
                comment='This is probably a Starforge or Dying Sun'))
    f.add(Block(theme=good_unique, item_level=82, rarity='Unique', base_type=['Vaal Gauntlets', 'Vaal Axe'],
                comment='Acuity+Disfavour from Atziri(They drop ilvl 82 from Atziri, div card version should never be on the ground anyway), put it here so we don\'t show other vaal gauntlets or vaal axes as GG'))
    f.add(Block(theme=good_unique, item_level=74, rarity='Unique', base_type='Spine Bow',
                comment='Reach of the Council(so we don\'t show Voltaxic as GG)'))

    good_breach_uniques = ['Ezomyte Tower Shield', 'Amber Amulet', 'Goathide Boots', 'Cutlass', 'Stibnite Flask', 'Void Axe',
                           'Ebony Tower Shield']
    decent_breach_uniques = ['Jingling Spirit Shield', 'Sage Wand', 'Abyssal Axe']

    f.add(Block(theme=good_unique, comment='Uniques that are usually 1ex+', rarity='Unique',
                base_type=['Occultist\'s Vestment', 'Jewelled Foil', 'Glorious Plate', 'Prismatic Jewel',
                           'Citrine Amulet', 'Gladiator Plate', 'Assassin\'s Garb', 'Golden Mantle',
                           'Sorcerer Boots', 'Crusader Boots', 'Murder Boots', 'Nightmare Bascinet',
                           'Deicide Mask', 'Champion Kite Shield', 'Vaal Sceptre', 'Judgement Staff',
                           'Prophecy Wand', 'Grand Mana Flask', 'Sapphire Flask', 'Silver Flask',
                           'Stibnite Flask', 'Topaz Flask', 'Siege Axe', 'Museum Map', 'Titanium Spirit Shield'] + good_breach_uniques))
    f.add(Block(theme=decent_unique, comment='Uniques that are usually 2c-1ex', rarity='Unique',
                base_type=['Onyx Amulet', 'Paua Ring', 'Unset Ring', 'Gold Ring', 'Two-Stone Ring',
                           'Moonstone Ring', 'Broadhead Arrow Quiver', 'Penetrating Arrow Quiver',
                           'Desert Brigandine', 'Savan', 'Vaal Regalia',
                           'Full Wyrmscale', 'Varnished Coat', 'Sacrificial Garb', 'Nubuck Boots',
                           'Sharkskin Boots', 'Slink Boots', 'Conjurer Boots', 'Deerskin Gloves',
                           'Strapped Mitts', 'Imperial Bow', 'Fiend Dagger', 'Slaughter Knife',
                           'Imperial Skean', 'Eternal Sword', 'Imperial Staff',
                           'Granite Flask'] + decent_breach_uniques))
    f.add(Block(theme=decent_unique, comment='Unique maps are almost always worth something', rarity='Unique',
                _class='Maps'))
    # @TODO: add more shit uniques
    # f.add(Block(theme=shit_unique, sockets=Comparer(6, '<'), linked_sockets=Comparer(5, '<'),
    #                      base_type=['Simple Robe', 'Strapped Boots'], rarity='Unique',
    #                      comment='Trash Uniques, no sound, same look as normal unique, make sure it has no other special stuff(which we would make sound for) @TODO: add more here'))
    f.add(Block(theme=unique, rarity='Unique'))

    f.add(Comment('Section: #0005 - Maps\n'))
    bonus_maps = {}
    for map_tier_setting in config.get('map_tiers', 'Strand Map,4\r\nPromenade Map,2\r\nQuay Map,1\r\nMesa Map,1').splitlines():
        split_setting = map_tier_setting.split(',')
        bonus_maps[split_setting[0]] = int(split_setting[1])

    for _map in get_all_maps():
        map_block = _map.make_block()
        map_block.set_theme(map_theme(_map.tier + bonus_maps.get(_map.base_name, 0)))
        f.add(map_block)

    f.add(Block(play_alert_sound=Sound(2), _class='Maps'))

    f.add(Block(theme=gg_fragment, _class='Map Fragments',
                base_type=['Mortal Hope', 'Mortal Ignorance', 'Fragment of the Phoenix',
                           'Fragment of the Minotaur', 'Fragment of the Chimera', 'Fragment of the Hydra']))
    f.add(Block(theme=good_fragment, _class='Map Fragments',
                base_type=['Mortal', 'Sacrifice at Midnight', 'Eber\'s Key', 'Inya\'s Key', 'Volkuur\'s Key',
                           'Yriel\'s Key', 'Breachstone']))
    f.add(Block(theme=fragment, _class='Map Fragments'))

    f.add(Comment('Section: #0006 - Currency + Essences\n'))
    f.add(Block(theme=gg, base_type=['Exalted Orb', 'Eternal Orb', 'Albino Rhoa Feather']))
    f.add(Block(theme=good_currency, base_type=['Deafening Essence', 'Shrieking Essence', 'Divine Orb', 'Unshaping Orb',
                                                'Essence of Hysteria', 'Essence of Insanity', 'Essence of Horror',
                                                'Essence of Delirium', 'Blessing']))
    f.add(Block(theme=decent_currency,
                base_type=['Cartographer\'s Sextant', 'Chaos Orb', 'Cartographer\'s Seal', 'Orb of Fusing',
                           'Orb of Regret', 'Regal Orb', 'Blessed Orb', 'Gemcutter\'s Prism',
                           'Orb of Scouring', 'Vaal Orb', 'Remnant of Corruption', 'Essence of']))
    f.add(Block(theme=Theme(text_color=Color(231, 180, 120),
                            background_color=Color(0, 0, 0, 180),
                            border_color=Color(231, 180, 120),
                            font_size=45),
                base_type='Perandus Coin'))
    f.add(Block(
            theme=Theme(text_color=Colors.BLOOD_RED, background_color=Color(0, 0, 0, 220), border_color=Colors.BLOOD_RED,
                        font_size=45),
            _class=['Stackable Currency'],
            base_type=['Splinter'],
    ))
    f.add(Block(theme=currency, base_type=['Orb of Alchemy', 'Silver Coin', 'Orb of Chance', 'Jeweller\'s Orb',
                                           'Orb of Alteration', 'Cartographer\'s Chisel']))
    wisdom_scrolls = int(config.get('wisdom_scrolls', '1'))
    portal_scrolls = int(config.get('portal_scrolls', '1'))
    if wisdom_scrolls == 1:
        f.add(Block(_class=['Currency'], base_type=['Wisdom']))
    elif wisdom_scrolls == 2:
        f.add(Block(_class=['Currency'], base_type=['Wisdom'], theme=shit_currency))
    elif wisdom_scrolls == 0:
        f.add(Block(_class=['Currency'], base_type=['Wisdom'], show=False))
    
    if portal_scrolls == 1:
        f.add(Block(_class=['Currency'], base_type=['Portal']))
    elif portal_scrolls == 2:
        f.add(Block(_class=['Currency'], base_type=['Portal'], theme=shit_currency))
    elif portal_scrolls == 0:
        f.add(Block(_class=['Currency'], base_type=['Portal'], show=False))

    f.add(Block(theme=shit_currency, _class=['Currency', 'Stackable Currency']))

    f.add(Comment('Section: #0007 - Divination Cards\n'))
    f.add(Block(theme=meh_div_cards, base_type='The Wolf\'s Shadow',
                comment='Added here so that "The Wolf" doesn\'t get confused with "The Wolf\'s Shadow"(Thanks Neversink for this tip!)'))
    f.add(Block(theme=gg_div_cards,
                base_type=['Abandoned Wealth', 'The Doctor', 'The Fiend', 'Mawr Blaidd', 'The Offering',
                           'The Brittle Emperor', 'The Harvester', 'The Last One Standing',
                           'The Dragon\'s Heart', 'The Ethereal', 'The Queen', 'The Enlightened', 'The Hunger',
                           'Pride Before the Fall', 'The King\'s Heart', 'The Vast', 'Wealth and Power',
                           'The Immortal', 'The Devastator', 'Hunter\'s Reward', 'The Spark and the Flame']))
    f.add(Block(theme=good_div_cards,
                base_type=['Bowyer\'s Dream', 'The Formless Sea', 'The Penitent', 'Heterochromia',
                           'Lucky Deck', 'The Stormcaller', 'The Wolf', 'The Artist', 'Earth Drinker',
                           'The Trial', 'The Celestial Justicar', 'The Surveyor', 'The Valkyrie',
                           'Chaotic Disposition', 'The Sephirot', 'The Void', 'The Dark Mage',
                           'The Dapper Prodigy', 'Time-Lost Relic', 'The Chains that Bind',
                           'Dialla\'s Subjugation', 'Emperor of Purity', 'The Soul', 'The Polymath', 'The Porcupine',
                           'The Saint\'s Treasure', 'The Wolven King\'s Bite']))
    f.add(Block(theme=meh_div_cards,
                base_type=['The Flora\'s Gift', 'Her Mask', 'Rain of Chaos', 'Thunderous Skies', 'The Gambler']))
    f.add(Block(theme=shit_div_cards,
                base_type=['The Rabid Rhoa', 'The Carrion Crow', 'Doedre\'s Madness', 'The Dragon',
                           'The One With All', 'The Scarred Meadow']))
    f.add(Block(theme=div_cards, _class='Divination Card'))

    f.add(Comment('Section: #0008 - Socket/Link Stuff\n'))
    f.add(Block(theme=quest_item, play_alert_sound=Sound(1), linked_sockets=5))
    f.add(Block(theme=six_socket_special, item_level=Comparer(75, '>='), sockets=Comparer(6, '>='), rarity='Rare'))
    f.add(Block(theme=six_socket, sockets=Comparer(6, '>=')))

    f.add(Comment('Section: #0009 - Gems\n'))
    gems = int(config.get('gems', '2'))
    if gems >= 1:
        f.add(Block(theme=gg_gems, _class='Skill Gems', base_type=['Empower', 'Enlighten'], quality=Comparer(10, '>=')))
        f.add(Block(theme=gg_gems, _class='Skill Gems', quality=Comparer(19, '>=')))
        f.add(Block(theme=quest_item, play_alert_sound=Sound(1), _class='Skill Gems', base_type=['Portal', 'Empower',
                                                                                                 'Enlighten',
                                                                                                 'Vaal Haste']))
        f.add(Block(theme=ok_quality_gems, _class='Skill Gems', quality=Comparer(13, '>=')))
        f.add(Block(theme=good_gems, _class='Skill Gems', base_type=['Vaal', 'Detonate Mines', 'Added Chaos Damage']))
        f.add(Block(theme=quality_gems, _class='Skill Gems', quality=Comparer(1, '>=')))
    if gems >= 2:
        f.add(Block(_class='Skill Gems'))

    f.add(Comment('Section: #0010 - Rare Evaluation\n'))
    f.add(Block(theme=rare_jewels, _class='Jewel', rarity='Rare'))
    f.add(Block(theme=rare_atlas_bases, item_level=Comparer(84, '>='), base_type=atlas_bases, rarity='Rare'))
    f.add(Block(theme=rare_max_ilvl_bases, item_level=Comparer(84, '>='), rarity='Rare',
                base_type=gg_es_bases + gg_spell_bases))
    f.add(Block(theme=rare_max_ilvl_bases, item_level=Comparer(84, '>='), rarity='Rare', _class=jewellery))
    f.add(Block(theme=rare_max_ilvl_bases, item_level=Comparer(84, '>='), rarity='Rare',
                base_type=good_spell_bases + good_armour_bases, set_font_size=38))
    f.add(Block(theme=rare_max_ilvl_bases, item_level=Comparer(83, '>='), rarity='Rare', base_type=gg_phys_bases))
    f.add(Block(theme=rare_max_ilvl_bases, item_level=Comparer(83, '>='), rarity='Rare', base_type=good_phys_bases,
                set_font_size=38))
    f.add(Block(theme=rare_max_ilvl_bases, item_level=Comparer(83, '>='), rarity='Rare', base_type='Sai',
                _class='Daggers', set_font_size=38))
    f.add(Block(theme=rare_atlas_bases, rarity='Rare', base_type=gg_atlas_bases))
    f.add(Block(theme=rare_atlas_bases, rarity='Rare', play_alert_sound=None, set_font_size=42,
                base_type=other_atlas_bases))
    f.add(Block(theme=rare_decent_ilvl_bases, rarity='Rare', base_type=good_phys_bases, item_level=Comparer(73, '>=')))
    f.add(Block(theme=rare_decent_ilvl_bases, item_level=Comparer(73, '>='), rarity='Rare', base_type='Sai',
                _class='Daggers'))
    f.add(Block(theme=rare_decent_ilvl_bases, item_level=Comparer(72, '>='), rarity='Rare',
                base_type=good_armour_bases + gg_es_bases))
    f.add(Block(theme=rare_good_bases, rarity='Rare',
                base_type=good_phys_bases + gg_es_bases + good_armour_bases + gg_spell_bases + good_spell_bases))
    ilvl_swap(f, Block(theme=rare_decent_ilvl_bases, item_level=Comparer(75, '>='), rarity='Rare', _class=jewellery,
                       set_font_size=40), rare_good_bases, set_font_size=40)
    ilvl_swap(f, Block(theme=rare_decent_ilvl_bases, set_font_size=35, rarity='Rare', item_level=Comparer(73, '>='),
                       drop_level=Comparer(59, '>='), _class=['Wands', 'Daggers', 'Sceptres']), rare_good_bases,
              set_font_size=35)
    f.add(Block(theme=rare_shit_bases, item_level=Comparer(65, '>='), drop_level=Comparer(55, '<='),
                _class=melee_only_classes, rarity='Rare'))
    ilvl_swap(f, Block(theme=rare_decent_ilvl_bases, item_level=Comparer(74, '>='), rarity='Rare', _class='Quivers',
                       set_font_size=35,
                       base_type=['Spike-Point Arrow Quiver', 'Broadhead Arrow Quiver', 'Two-Point Arrow Quiver']),
              lower_theme=rare_good_bases, set_font_size=35)
    ilvl_swap(f, Block(theme=rare_decent_ilvl_bases, item_level=Comparer(72, '>='), drop_level=Comparer(44, '>='),
                       rarity='Rare', _class=['Gloves', 'Boots', 'Helmets'], set_font_size=35),
              lower_theme=rare_good_bases,
              set_font_size=35)
    f.add(Block(theme=rare_shit_bases, item_level=Comparer(65, '>='), drop_level=Comparer(15, '<='),
                _class=['Gloves', 'Boots', 'Helmets'],
                rarity='Rare'))
    f.add(Block(theme=rare_shit_bases, item_level=Comparer(65, '>='), drop_level=Comparer(50, '<='), _class='Shields',
                rarity='Rare'))
    f.add(
        Block(theme=rare_shit_bases, item_level=Comparer(65, '>='), drop_level=Comparer(47, '<='), _class='Body Armour',
              rarity='Rare'))
    f.add(Block(theme=rare_good_bases, set_font_size=45, item_level=Comparer(30, '<'), rarity='Rare', _class='Boots'))
    f.add(
        Block(theme=rare_good_bases, item_level=Comparer(65, '<'), rarity='Rare', _class=['Boots', 'Helmets', 'Gloves',
                                                                                          'Sceptres', 'Daggers',
                                                                                          'Wands']))
    f.add(Block(theme=rare_good_bases, item_level=Comparer(10, '<'), rarity='Rare'))
    # nice example of what you can do with PoEFilter
    for drop_level in range(5, 56):
        f.add(Block(theme=rare_good_bases, item_level=Comparer(drop_level + 10, '<'),
                    drop_level=Comparer(drop_level, '>'),
                    rarity='Rare', set_font_size=35))

    f.add(Block(theme=Theme(background_color=Colors.BLACK, border_color=Color(150, 150, 150), font_size=35),
                item_level=Comparer(20, '<'), rarity='Rare'))
    f.add(Block(theme=Theme(background_color=Color(0, 0, 0, 180), border_color=Color(150, 150, 150), font_size=35),
                item_level=Comparer(65, '<'), rarity='Rare'))
    f.add(Block(theme=Theme(background_color=Color(0, 0, 0, 225), border_color=Color(150, 150, 150), font_size=26),
                rarity='Rare', width=Comparer(2, '>='), height=Comparer(4, '>=')))
    small_sizes(f, Block(rarity='Rare', theme=Theme(background_color=Colors.BLACK, border_color=Color(150, 150, 150),
                                                    font_size=35)))
    f.add(Block(theme=Theme(background_color=Color(0, 0, 0, 180), border_color=Color(150, 150, 150), font_size=35),
                rarity='Rare'))

    f.add(Comment('Section: #0011 - Normal and Magic Items\n'))
    show_jewellery = int(config.get('jewellery', '2'))
    if animate_weapon:
        f.add(Block(theme=Theme(background_color=Color(0, 0, 0, 0), border_color=Colors.BLOOD_RED, text_color=Colors.BLOOD_RED), comment='Animate Weapon', rarity='Normal', _class=['One Hand', 'Two Hand', 'Staves', 'Daggers', 'Thrusting', 'Sceptres', 'Claws']))
    f.add(Block(comment='Redblade(potentially)', rarity='Magic', _class='Helmets', identified=True,
                set_border_color=Color(210, 0, 0)))
    f.add(Block(theme=white_atlas_bases, base_type=atlas_bases, item_level=Comparer(84, '>=')))
    f.add(Block(theme=white_gg_bases, item_level=Comparer(84, '>='), base_type=gg_es_bases + gg_spell_bases))
    f.add(Block(theme=white_gg_bases, item_level=Comparer(84, '>='), _class=jewellery))
    f.add(Block(theme=white_ok_bases, item_level=Comparer(84, '>='), base_type=good_spell_bases + good_armour_bases))
    f.add(Block(theme=white_gg_bases, item_level=Comparer(83, '>='), base_type=gg_phys_bases))
    f.add(Block(theme=white_ok_bases, item_level=Comparer(83, '>='), base_type=good_phys_bases))
    f.add(Block(theme=white_ok_bases, item_level=Comparer(83, '>='), base_type='Sai', _class='Daggers'))
    f.add(Block(theme=white_atlas_bases, base_type=gg_atlas_bases))
    f.add(Block(theme=white_atlas_bases, base_type=other_atlas_bases, play_alert_sound=None, set_font_size=36))
    chromatic_recipe = int(config.get('chromatic_recipe', '2'))
    if chromatic_recipe >= 1:
        small_sizes(f, Block(theme=chromatic_item, socket_group='RGB'))
    if chromatic_recipe == 2:
        f.add(Block(theme=chromatic_item, set_font_size=30, socket_group='RGB'))
    f.add(Block(theme=chance_item, rarity='Normal', base_type=['Sorcerer Boots', 'Occultist\'s Vestment', 'Sapphire Flask',
                                                               'Ebony Tower Shield']))
    if show_jewellery >= 2:
        f.add(Block(theme=alch_base, item_level=Comparer(67, '>='), rarity='Normal', _class=jewellery,
                    base_type=['Onyx', 'Ruby', 'Sapphire', 'Topaz', 'Two-Stone', 'Diamond', 'Prismatic', 'Unset', 'Gold',
                               'Citrine', 'Turquoise', 'Agate', 'Coral Ring', 'Moonstone', 'Leather', 'Heavy', 'Amber',
                               'Jade', 'Lapis', 'Rustic', 'Iron Ring']))
    if show_jewellery >= 1:
        f.add(Block(theme=magic_jewellery, item_level=Comparer(67, '>='), rarity='Magic', _class=jewellery))
    f.add(Block(theme=magic_jewel, _class='Jewel'))

    f.add(Comment('Section: #0012 - Flasks\n'))
    flasks = int(config.get('flasks', '2'))
    if flasks >= 1:
        f.add(Block(theme=high_quality_flask, quality=Comparer(18, '>='), rarity='Magic', _class='Utility Flasks'))
        f.add(Block(theme=high_quality_flask, quality=Comparer(15, '>='), rarity='Normal', _class='Utility Flasks'))
        f.add(Block(theme=high_quality_flask, quality=Comparer(1, '>='), _class='Utility Flasks', set_font_size=38))
    f.add(Block(theme=utility_flask, _class='Utility Flasks', item_level=Comparer(10, '<='), set_font_size=38))
    f.add(Block(theme=utility_flask, _class='Utility Flasks', item_level=Comparer(25, '<='), set_font_size=37))
    f.add(Block(theme=utility_flask, _class='Utility Flasks', item_level=Comparer(50, '<='), set_font_size=36))
    if flasks >= 2:
        f.add(Block(theme=utility_flask, _class='Utility Flasks'))
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
    f.add(Block(theme=early_survival, item_level=Comparer(12, '<'),
                base_type=['Coral Ring', 'Sapphire Ring', 'Leather Belt']))
    f.add(Block(theme=early_survival, item_level=Comparer(12, '<'), set_font_size=38,
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

    f.add(Comment('Section: #0014 - Failsafe\n'))
    add_failsafe(f)
    return f


def main():
    f = generate_xai_filter()

    with open('Xai.filter', encoding='utf-8', mode='w') as file:
        file.write(str(f))


def get_themes():
    map_blue = Color(30, 144, 255)
    decent_unique = Theme(text_color=Colors.WHITE, background_color=Colors.UNIQUE, border_color=Colors.WHITE,
                          font_size=45, alert_sound=6)
    good_unique = Theme(text_color=Colors.UNIQUE, background_color=Color(255, 255, 255), border_color=Colors.UNIQUE,
                        font_size=45, alert_sound=5)
    shit_unique = Theme(text_color=Colors.UNIQUE, border_color=Colors.UNIQUE, background_color=Color(0, 0, 0, 0.5),
                        font_size=35)
    unique = Theme(text_color=Colors.UNIQUE, border_color=Colors.UNIQUE, font_size=40, alert_sound=3)
    special_quest_item = Theme(text_color=Colors.WHITE, background_color=Color(0, 128, 0), font_size=45,
                               alert_sound=1)
    quest_item = Theme(text_color=Color(50, 230, 100), border_color=Color(74, 230, 58), font_size=45)
    gg = Theme(text_color=Color(210, 0, 220), background_color=Colors.WHITE, border_color=Color(208, 32, 144),
               font_size=45, alert_sound=8)
    good_currency = Theme(text_color=Colors.WHITE, background_color=Color(30, 144, 255), border_color=Colors.WHITE,
                          font_size=45, alert_sound=5)
    decent_currency = Theme(text_color=Colors.BLACK, background_color=Color(255, 165, 0), border_color=Colors.BLACK,
                            font_size=45, alert_sound=1)
    currency = Theme(text_color=Color(163, 141, 109), background_color=Colors.BLACK, border_color=Colors.WHITE,
                     font_size=45)
    shit_currency = Theme(text_color=Color(163, 141, 109), background_color=Color(0, 0, 0, 180),
                          border_color=Color(163, 141, 109), font_size=45)
    shaper_maps = Theme(text_color=Colors.BLOOD_RED, background_color=Colors.WHITE, border_color=Colors.BLOOD_RED,
                        font_size=45, alert_sound=2)

    def map_theme(tier):
        font_size = min(45, max(tier + 32, 33))  # kind of put the font size between 33 and 45
        val = 1.0 - min((float(tier) * 17.0) / 255.0, 1.0)
        colors = hsv_to_rgb(val / 3.0, 1.0, 1.0)
        shade_color = Color(colors[0], colors[1], colors[2])
        theme = Theme(font_size=font_size, background_color=Color(0, 30, 255), text_color=shade_color,
                      border_color=shade_color)
        if tier > 1:
            theme.alert_sound = Sound(2)
        return theme

    gg_fragment = Theme(text_color=Colors.BLACK, background_color=Colors.WHITE, border_color=Colors.BLACK, font_size=45,
                        alert_sound=6)
    good_fragment = Theme(text_color=Colors.BLACK, background_color=Colors.BLOOD_RED, border_color=Colors.BLACK,
                          font_size=45,
                          alert_sound=2)
    fragment = Theme(text_color=Colors.BLOOD_RED, background_color=Colors.BLACK, border_color=Colors.BLOOD_RED,
                     font_size=38,
                     alert_sound=2)
    meh_div_cards = Theme(text_color=Colors.BLACK, background_color=Color(200, 200, 200, 180), border_color=map_blue,
                          font_size=45)
    gg_div_cards = Theme(text_color=Colors.WHITE, background_color=Color(208, 32, 144), border_color=Colors.WHITE,
                         font_size=45, alert_sound=5)
    good_div_cards = Theme(text_color=Colors.WHITE, background_color=map_blue, border_color=Colors.WHITE, font_size=45,
                           alert_sound=6)
    shit_div_cards = Theme(text_color=Colors.BLACK, background_color=Color(200, 200, 200, 180),
                           border_color=Colors.BLACK,
                           font_size=35)
    div_cards = Theme(text_color=Colors.BLACK, background_color=Color(200, 200, 200, 180), border_color=map_blue,
                      font_size=45, alert_sound=3)
    six_socket = Theme(text_color=Colors.WHITE, background_color=Colors.GRAY, border_color=Colors.WHITE, font_size=45,
                       alert_sound=7)
    six_socket_special = Theme(text_color=Color(255, 200, 0), background_color=Colors.GRAY,
                               border_color=Color(255, 200, 0),
                               font_size=45, alert_sound=7)
    gg_gems = Theme(text_color=Colors.GEM, background_color=Colors.WHITE, border_color=Colors.GEM, font_size=45,
                    alert_sound=5)
    ok_quality_gems = Theme(border_color=Colors.GEM, font_size=45, alert_sound=1)
    quality_gems = Theme(border_color=Colors.GEM)
    good_gems = Theme(border_color=Colors.BLOOD_RED)
    rare_jewels = Theme(text_color=Colors.YELLOW, background_color=Color(75, 75, 0), border_color=Colors.YELLOW,
                        font_size=45)
    rare_atlas_bases = Theme(text_color=Color(255, 255, 119), background_color=Color(74, 230, 58),
                             border_color=Color(255, 255, 119),
                             font_size=45, alert_sound=5)
    rare_max_ilvl_bases = Theme(text_color=Color(0, 128, 0), background_color=Color(255, 200, 0),
                                border_color=Color(0, 128, 0),
                                font_size=45)
    rare_decent_ilvl_bases = Theme(text_color=Color(255, 190, 0), background_color=Color(30, 90, 45),
                                   border_color=Colors.WHITE, font_size=38)
    rare_good_bases = Theme(background_color=Color(30, 90, 45), border_color=Color(255, 255, 119), font_size=38)
    rare_shit_bases = Theme(background_color=Color(120, 20, 20, 150), border_color=Color(150, 150, 150, 150),
                            font_size=25)
    white_atlas_bases = Theme(text_color=Color(255, 255, 119), border_color=Color(255, 255, 119),
                              background_color=Colors.BLACK, font_size=45, alert_sound=1)
    white_gg_bases = Theme(border_color=Color(255, 255, 0), font_size=40, background_color=Colors.BLACK)
    white_ok_bases = Theme(border_color=Color(255, 255, 0, 180), background_color=Color(0, 0, 0, 180), font_size=38)
    chromatic_item = Theme(border_color=Color(27, 162, 155), background_color=Color(107, 107, 107), font_size=36)
    chance_item = Theme(border_color=Color(74, 230, 58))
    alch_base = Theme(border_color=Color(255, 190, 0, 150), font_size=32)
    magic_jewellery = Theme(border_color=Colors.BLACK, font_size=28, background_color=Color(0, 0, 0, 165))
    magic_jewel = Theme(text_color=Color(0, 100, 255), background_color=Color(0, 40, 60),
                        border_color=Color(0, 75, 250),
                        font_size=36)
    high_quality_flask = Theme(background_color=Color(75, 75, 75), border_color=Colors.WHITE, font_size=45)
    utility_flask = Theme(background_color=Color(75, 75, 75), border_color=Colors.BLACK)
    early_survival = Theme(border_color=Colors.BLOOD_RED, font_size=40)
    return alch_base, chance_item, chromatic_item, currency, decent_currency, decent_unique, div_cards, early_survival, fragment, gg, gg_div_cards, gg_fragment, gg_gems, good_currency, good_div_cards, good_fragment, good_gems, good_unique, high_quality_flask, magic_jewel, magic_jewellery, meh_div_cards, ok_quality_gems, quality_gems, quest_item, rare_atlas_bases, rare_decent_ilvl_bases, rare_good_bases, rare_jewels, rare_max_ilvl_bases, rare_shit_bases, shaper_maps, shit_currency, shit_div_cards, shit_unique, six_socket, six_socket_special, special_quest_item, unique, utility_flask, white_atlas_bases, white_gg_bases, white_ok_bases, map_theme


if __name__ == '__main__':
    main()
