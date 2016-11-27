from collections import OrderedDict

from block import Block
from comment import Comment
from filter import Filter
from helpers.base_types_and_classes import atlas_bases, gg_es_bases, gg_spell_bases, jewellery, good_armour_bases, good_spell_bases, \
    gg_phys_bases, good_phys_bases, gg_atlas_bases, other_atlas_bases, melee_only_classes
from helpers.colors import Colors
from helpers.general import ilvl_swap
from helpers.map import get_maps_by_tier
from properties.color import Color
from properties.comparer import Comparer
from properties.sound import Sound
from theme import Theme


def main():
    f = Filter()
    
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
    currency = Theme(text_color=Color(163, 141, 109), background_color=Colors.BLACK, border_color=Colors.WHITE, font_size=45)
    shit_currency = Theme(text_color=Color(163, 141, 109), background_color=Color(0, 0, 0, 180),
                          border_color=Color(163, 141, 109), font_size=45)

    shaper_maps = Theme(text_color=Colors.BLOOD_RED, background_color=Colors.WHITE, border_color=Colors.BLOOD_RED,
                        font_size=45, alert_sound=2)
    gg_maps = Theme(text_color=Colors.BLOOD_RED, background_color=Color(184, 218, 242), border_color=Colors.BLOOD_RED,
                    font_size=45, alert_sound=2)
    good_maps = Theme(text_color=Color(150, 0, 0), background_color=map_blue, border_color=Color(150, 0, 0),
                      font_size=42, alert_sound=2)
    ok_maps = Theme(text_color=map_blue, background_color=Color(0, 0, 0), border_color=map_blue, font_size=40,
                    alert_sound=2)
    maps = Theme(text_color=Colors.WHITE, background_color=Colors.BLACK, border_color=Colors.WHITE, alert_sound=2)

    gg_fragment = Theme(text_color=Colors.BLACK, background_color=Colors.WHITE, border_color=Colors.BLACK, font_size=45,
                        alert_sound=6)
    good_fragment = Theme(text_color=Colors.BLACK, background_color=Colors.BLOOD_RED, border_color=Colors.BLACK, font_size=45,
                          alert_sound=2)
    fragment = Theme(text_color=Colors.BLOOD_RED, background_color=Colors.BLACK, border_color=Colors.BLOOD_RED, font_size=38,
                     alert_sound=2)

    meh_div_cards = Theme(text_color=Colors.BLACK, background_color=Color(200, 200, 200, 180), border_color=map_blue,
                          font_size=45)
    gg_div_cards = Theme(text_color=Colors.WHITE, background_color=Color(208, 32, 144), border_color=Colors.WHITE,
                         font_size=45, alert_sound=5)
    good_div_cards = Theme(text_color=Colors.WHITE, background_color=map_blue, border_color=Colors.WHITE, font_size=45,
                           alert_sound=6)
    shit_div_cards = Theme(text_color=Colors.BLACK, background_color=Color(200, 200, 200, 180), border_color=Colors.BLACK,
                           font_size=35)
    div_cards = Theme(text_color=Colors.BLACK, background_color=Color(200, 200, 200, 180), border_color=map_blue,
                      font_size=45, alert_sound=3)

    six_socket = Theme(text_color=Colors.WHITE, background_color=Colors.GRAY, border_color=Colors.WHITE, font_size=45,
                       alert_sound=7)
    six_socket_special = Theme(text_color=Color(255, 200, 0), background_color=Colors.GRAY, border_color=Color(255, 200, 0),
                               font_size=45, alert_sound=7)

    gg_gems = Theme(text_color=Colors.GEM, background_color=Colors.WHITE, border_color=Colors.GEM, font_size=45, alert_sound=5)
    ok_quality_gems = Theme(border_color=Colors.GEM, font_size=45, alert_sound=1)
    quality_gems = Theme(border_color=Colors.GEM)
    good_gems = Theme(border_color=Colors.BLOOD_RED)

    rare_jewels = Theme(text_color=Colors.YELLOW, background_color=Color(75, 75, 0), border_color=Colors.YELLOW, font_size=45)
    rare_atlas_bases = Theme(text_color=Color(255, 255, 119), background_color=Color(74, 230, 58), border_color=Color(255, 255, 119),
                            font_size=45, alert_sound=5)
    rare_max_ilvl_bases = Theme(text_color=Color(0, 128, 0), background_color=Color(255, 200, 0), border_color=(0, 128, 0),
                           font_size=45)
    rare_decent_ilvl_bases = Theme(text_color=Color(255, 190, 0), background_color=Color(30, 90, 45), border_color=Colors.WHITE, font_size=38)
    rare_good_bases = Theme(background_color=Color(30, 90, 45), border_color=Color(255, 255, 119), font_size=38)
    rare_shit_bases = Theme(background_color=Color(120, 20, 20, 150), border_color=Color(150, 150, 150, 150), font_size=25)


    f.add(Comment('Section: #0001 - Special Stuff\n'))
    f.add(Block(theme=decent_unique,
                         comment='Tabula, we have to put this before everything cause our 6L block will override otherwise',
                         socket_group='W'*6,
                         rarity='Unique'))
    f.add(Block(theme=special_quest_item, _class='Quest Items', base_type='Shaper\'s Orb'))
    f.add(Block(theme=quest_item, _class=['Quest Items', 'Microtransactions']))
    # @TODO: Add more base types
    f.add(Block(theme=gg, item_level=1, rarity='Normal', base_type=['Glass Shank', 'Driftwoord Wand'], play_alert_sound=None,
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
    f.add(Block(theme=good_unique, comment='Uniques that are usually 1ex+', rarity='Unique',
                         base_type=['Occultist\'s Vestment', 'Jewelled Foil', 'Glorious Plate', 'Prismatic Jewel',
                                    'Citrine Amulet', 'Gladiator Plate', 'Assassin\'s Garb', 'Golden Mantle',
                                    'Sorcerer Boots', 'Crusader Boots', 'Murder Boots', 'Nightmare Bascinet',
                                    'Deicide Mask', 'Champion Kite Shield', 'Gavel', 'Vaal Sceptre', 'Judgement Staff',
                                    'Prophecy Wand', 'Grand Mana Flask', 'Sapphire Flask', 'Granite Flask',
                                    'Silver Flask', 'Stibnite Flask', 'Topaz Flask', 'Siege Axe', 'Museum Map']))
    f.add(Block(theme=decent_unique, comment='Uniques that are usually 2c-1ex', rarity='Unique',
                         base_type=['Onyx Amulet', 'Paua Ring', 'Unset Ring', 'Gold Ring', 'Two-Stone Ring',
                                    'Moonstone Ring', 'Broadhead Arrow Quiver', 'Penetrating Arrow Quiver',
                                    'Spike-Point Arrow Quiver', 'Desert Brigandine', 'Savan', 'Vaal Regalia',
                                    'Full Wyrmscale', 'Varnished Coat', 'Sacrificial Garb', 'Nubuck Boots',
                                    'Sharkskin Boots', 'Slink Boots', 'Conjurer Boots', 'Deerskin Gloves',
                                    'Strapped Mitts', 'Imperial Bow', 'Fiend Dagger', 'Slaughter Knife',
                                    'Imperial Skean', 'Eternal Sword', 'Imperial Staff']))
    f.add(Block(theme=decent_unique, comment='Unique maps are almost always worth something', rarity='Unique',
                         _class='Maps'))
    # @TODO: add more shit uniques
    f.add(Block(theme=shit_unique, sockets=Comparer(6, '<'), linked_sockets=Comparer(5, '<'),
                         base_type=['Simple Robe', 'Strapped Boots'], rarity='Unique',
                         comment='Trash Uniques, no sound, same look as normal unique, make sure it has no other special stuff(which we would make sound for) @TODO: add more here'))
    f.add(Block(theme=unique, rarity='Unique'))

    f.add(Comment('Section: #0005 - Maps\n'))
    maps_list = OrderedDict(sorted(get_maps_by_tier().items(), reverse=True))
    for tier in maps_list:
        drop_level = maps_list[tier][0].drop_level

        block_args = {'drop_level': Comparer(drop_level, '>='), '_class': 'Maps'}
        if tier >= 15:
            block_args['theme'] = shaper_maps
        elif tier >= 12:
            block_args['theme'] = gg_maps
        elif tier >= 9:
            block_args['theme'] = good_maps
        elif tier >= 5:
            block_args['theme'] = ok_maps
        else:
            block_args['theme'] = maps
            block_args['set_font_size'] = drop_level - 32
            if tier == 1:
                block_args['play_alert_sound'] = None

        f.add(Block(**block_args))

    f.add(Block(theme=gg_fragment, _class='Map Fragments',
                         base_type=['Mortal Hope', 'Mortal Ignorance', 'Fragment of the Phoenix',
                                    'Fragment of the Minotaur', 'Fragment of the Chimera', 'Fragment of the Hydra']))
    f.add(Block(theme=good_fragment, _class='Map Fragments',
                         base_type=['Mortal', 'Sacrifice at Midnight', 'Eber\'s Key', 'Inya\'s Key', 'Volkuur\'s Key',
                                    'Yriel\'s Key']))
    f.add(Block(theme=fragment, _class='Map Fragments'))

    f.add(Comment('Section: #0006 - Currency + Essences\n'))
    f.add(Block(theme=gg, base_type=['Exalted Orb', 'Eternal Orb', 'Albino Rhoa Feather']))
    f.add(Block(theme=good_currency, base_type=['Deafening Essence', 'Shrieking Essence', 'Divine Orb',
                                                         'Unshaping Orb', 'Essence of Hysteria', 'Essence of Insanity',
                                                         'Essence of Horror', 'Essence of Delirium']))
    f.add(Block(theme=decent_currency,
                         base_type=['Cartographer\'s Sextant', 'Chaos Orb', 'Cartographer\'s Seal', 'Orb of Fusing',
                                    'Orb of Regret', 'Regal Orb', 'Blessed Orb', 'Gemcutter\'s Prism',
                                    'Orb of Scouring', 'Vaal Orb', 'Remnant of Corruption', 'Essence of']))
    f.add(Block(theme=Theme(text_color=Color(231, 180, 120),
                                     background_color=Color(0, 0, 0, 180),
                                     border_color=Color(231, 180, 120),
                                     font_size=45),
                         base_type='Perandus Coin'))
    f.add(Block(theme=currency, base_type=['Orb of Alchemy', 'Silver Coin', 'Orb of Chance', 'Jeweller\'s Orb',
                                                    'Orb of Alteration', 'Cartographer\'s Chisel']))
    f.add(Block(theme=shit_currency, _class=['Currency', 'Stackable Currency']))

    f.add(Comment('Section: #0007 - Divination Cards\n'))
    f.add(Block(theme=meh_div_cards, base_type='The Wolf\'s Shadow',
                         comment='Added here so that "The Wolf" doesn\'t get confused with "The Wolf\'s Shadow"(Thanks Neversink for this tip!)'))
    f.add(Block(theme=gg_div_cards,
                         base_type=['Abandoned Wealth', 'The Doctor', 'The Fiend', 'Mawr Blaidd', 'The Offering',
                                    'The Brittle Emperor', 'The Harvester', 'The Last One Standing',
                                    'The Dragon\'s Heart', 'The Ethereal', 'The Queen', 'The Enlightened', 'The Hunger',
                                    'Pride Before the Fall', 'The King\'s Heart', 'The Vast', 'Wealth and Power',
                                    'The Immortal', 'The Devastator', 'Hunter\'s Reward']))
    f.add(Block(theme=good_div_cards,
                         base_type=['Bowyer\'s Dream', 'The Formless Sea', 'The Penitent', 'Heterochromia',
                                    'Lucky Deck', 'The Stormcaller', 'The Wolf', 'The Artist', 'Earth Drinker',
                                    'The Trial', 'The Celestial Justicar', 'The Surveyor', 'The Valkyrie',
                                    'Chaotic Disposition', 'The Sephirot', 'The Void', 'The Dark Mage',
                                    'The Dapper Prodigy', 'Time-Lost Relic', 'The Chains that Bind',
                                    'Dialla\'s Subjugation', 'Emperor of Purity', 'The Soul']))
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
    f.add(Block(theme=gg_gems, _class='Skill Gems', base_type=['Empower', 'Enlighten'], quality=Comparer(10, '>=')))
    f.add(Block(theme=gg_gems, _class='Skill Gems', quality=Comparer(19, '>=')))
    f.add(Block(theme=quest_item, play_alert_sound=Sound(1), _class='Skill Gems', base_type=['Portal', 'Empower',
                                                                                                      'Enlighten', 'Vaal Haste']))
    f.add(Block(theme=ok_quality_gems, _class='Skill Gems', quality=Comparer(13, '>=')))
    f.add(Block(theme=good_gems, _class='Skill Gems', base_type=['Vaal', 'Detonate Mines', 'Added Chaos Damage']))
    f.add(Block(theme=quality_gems, _class='Skill Gems', quality=Comparer(1, '>=')))
    f.add(Block(_class='Skill Gems'))

    f.add(Comment('Section: #0010 - Rare Evaluation\n'))
    f.add(Block(theme=rare_jewels, _class='Jewel', rarity='Rare'))
    f.add(Block(theme=rare_atlas_bases, item_level=Comparer(84, '>='), base_type=atlas_bases, rarity='Rare'))
    f.add(Block(theme=rare_max_ilvl_bases, item_level=Comparer(84, '>='), rarity='Rare', base_type=gg_es_bases + gg_spell_bases))
    f.add(Block(theme=rare_max_ilvl_bases, item_level=Comparer(84, '>='), rarity='Rare', _class=jewellery))
    f.add(Block(theme=rare_max_ilvl_bases, item_level=Comparer(84, '>='), rarity='Rare',
                         base_type=good_spell_bases + good_armour_bases, set_font_size=38))
    f.add(Block(theme=rare_max_ilvl_bases, item_level=Comparer(83, '>='), rarity='Rare', base_type=gg_phys_bases))
    f.add(Block(theme=rare_max_ilvl_bases, item_level=Comparer(83, '>='), rarity='Rare', base_type=good_phys_bases,
                         set_font_size=38))
    f.add(Block(theme=rare_max_ilvl_bases, item_level=Comparer(83, '>='), rarity='Rare', base_type='Sai',
                         _class='Daggers', set_font_size=38))
    f.add(Block(theme=rare_atlas_bases, rarity='Rare', base_type=gg_atlas_bases))
    f.add(Block(theme=rare_atlas_bases, rarity='Rare', play_alert_sound=None, set_font_size=42, base_type=other_atlas_bases))
    f.add(Block(theme=rare_decent_ilvl_bases, rarity='Rare', base_type=good_phys_bases, item_level=Comparer(73, '>=')))
    f.add(Block(theme=rare_decent_ilvl_bases, item_level=Comparer(73, '>='), rarity='Rare', base_type='Sai', _class='Daggers'))
    f.add(Block(theme=rare_decent_ilvl_bases, item_level=Comparer(72, '>='), rarity='Rare', base_type=good_armour_bases + gg_es_bases))
    f.add(Block(theme=rare_good_bases, rarity='Rare', base_type=good_phys_bases + gg_es_bases + good_armour_bases + gg_spell_bases + good_spell_bases))
    ilvl_swap(f, Block(theme=rare_decent_ilvl_bases, item_level=Comparer(75, '>='), rarity='Rare', _class=jewellery, set_font_size=40), rare_good_bases, set_font_size=40)
    ilvl_swap(f, Block(theme=rare_decent_ilvl_bases, set_font_size=35, rarity='Rare', item_level=Comparer(73, '>='),
              drop_level=Comparer(59, '>='), _class=['Wands', 'Daggers', 'Sceptres']), rare_good_bases, set_font_size=35)
    f.add(Block(theme=rare_shit_bases, item_level=Comparer(65, '>='), drop_level=Comparer(55, '<='),
                         _class=melee_only_classes, rarity='Rare'))
    ilvl_swap(f, Block(theme=rare_decent_ilvl_bases, item_level=Comparer(74, '>='), rarity='Rare', _class='Quivers', set_font_size=35,
                       base_type=['Spike-Point Arrow Quiver', 'Broadhead Arrow Quiver', 'Two-Point Arrow Quiver']),
              lower_theme=rare_good_bases, set_font_size=35)
    ilvl_swap(f, Block(theme=rare_decent_ilvl_bases, item_level=Comparer(72, '>='), drop_level=Comparer(44, '>='),
                       rarity='Rare', _class=['Gloves', 'Boots', 'Helmets'], set_font_size=35), lower_theme=rare_good_bases,
              set_font_size=35)
    f.add(Block(theme=rare_shit_bases, item_level=Comparer(65, '>='), drop_level=Comparer(15, '<='), _class=['Gloves', 'Boots', 'Helmets'],
                rarity='Rare'))
    f.add(Block(theme=rare_shit_bases, item_level=Comparer(65, '>='), drop_level=Comparer(50, '<='), _class='Shields',
                rarity='Rare'))
    f.add(Block(theme=rare_shit_bases, item_level=Comparer(65, '>='), drop_level=Comparer(47, '<='), _class='Body Armour',
                rarity='Rare'))
    f.add(Block(theme=rare_good_bases, set_font_size=45, item_level=Comparer(30, '<'), rarity='Rare', _class='Boots'))
    f.add(Block(theme=rare_good_bases, item_level=Comparer(65, '<'), rarity='Rare', _class=['Boots', 'Helmets', 'Gloves',
                                                                                            'Sceptres', 'Daggers', 'Wands']))
    f.add(Block(theme=rare_good_bases, item_level=Comparer(10, '<'), rarity='Rare'))
    # nice example of what you can do with PoEFilter
    for drop_level in range(5, 60, 5):
        f.add(Block(theme=rare_good_bases, item_level=Comparer(drop_level + 10, '<'), drop_level=Comparer(drop_level, '>'),
                    rarity='Rare', set_font_size=35))

    f.add(Block(theme=Theme(background_color=Colors.BLACK, border_color=Color(150, 150, 150), font_size=35),
                item_level=Comparer(20, '<'), rarity='Rare'))
    f.add(Block(theme=Theme(background_color=Color(0, 0, 0, 180), border_color=Color(150, 150, 150), font_size=35),
                item_level=Comparer(65, '<'), rarity='Rare'))

    with open('xai.filter', 'w') as file:
        file.write(str(f))

if __name__ == '__main__':
    main()
