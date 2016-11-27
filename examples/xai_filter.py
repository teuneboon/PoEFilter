from block import Block
from comment import Comment
from filter import Filter
from helpers.colors import Colors
from properties.color import Color
from properties.comparer import Comparer
from properties.sound import Sound
from theme import Theme


def main():
    xai_filter = Filter()
    
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

    xai_filter.add(Comment('Section: #0001 - Special Stuff\n'))
    xai_filter.add(Block(theme=decent_unique,
                         comment='Tabula, we have to put this before everything cause our 6L block will override otherwise',
                         socket_group='W'*6,
                         rarity='Unique'))
    xai_filter.add(Block(theme=special_quest_item, _class='Quest Items', base_type='Shaper\'s Orb'))
    xai_filter.add(Block(theme=quest_item, _class=['Quest Items', 'Microtransactions']))
    # @TODO: Add more base types
    xai_filter.add(Block(theme=gg, item_level=1, rarity='Normal', base_type=['Glass Shank', 'Driftwoord Wand'], play_alert_sound=None,
                         comment='Make ilvl 1 of starter weapons ugly so people know they forgot their racing filter @TODO: add others'))

    xai_filter.add(Comment('Section: #0002 - Labyrinth\n'))
    xai_filter.add(Block(theme=special_quest_item, base_type='Offering to the Goddess'))
    xai_filter.add(Block(theme=quest_item, _class='Labyrinth', play_alert_sound=Sound(1)))

    xai_filter.add(Comment('Section: #0003 - GG!!!\n'))
    xai_filter.add(Block(theme=gg, base_type=['Mirror of Kalandra', 'Fishing Rod']))
    xai_filter.add(Block(theme=gg, linked_sockets=Comparer(6, '>=')))

    xai_filter.add(Comment('Section: #0004 - Uniques\n'))
    xai_filter.add(Block(theme=good_unique, item_level=84, rarity='Unique', base_type=['Infernal Sword', 'Ruby Flask'],
                         comment='This is probably a Starforge or Dying Sun'))
    xai_filter.add(Block(theme=good_unique, item_level=82, rarity='Unique', base_type=['Vaal Gauntlets', 'Vaal Axe'],
                         comment='Acuity+Disfavour from Atziri(They drop ilvl 82 from Atziri, div card version should never be on the ground anyway), put it here so we don\'t show other vaal gauntlets or vaal axes as GG'))
    xai_filter.add(Block(theme=good_unique, item_level=74, rarity='Unique', base_type='Spine Bow',
                         comment='Reach of the Council(so we don\'t show Voltaxic as GG)'))
    xai_filter.add(Block(theme=good_unique, comment='Uniques that are usually 1ex+', rarity='Unique',
                         base_type=['Occultist\'s Vestment', 'Jewelled Foil', 'Glorious Plate', 'Prismatic Jewel',
                                    'Citrine Amulet', 'Gladiator Plate', 'Assassin\'s Garb', 'Golden Mantle',
                                    'Sorcerer Boots', 'Crusader Boots', 'Murder Boots', 'Nightmare Bascinet',
                                    'Deicide Mask', 'Champion Kite Shield', 'Gavel', 'Vaal Sceptre', 'Judgement Staff',
                                    'Prophecy Wand', 'Grand Mana Flask', 'Sapphire Flask', 'Granite Flask',
                                    'Silver Flask', 'Stibnite Flask', 'Topaz Flask', 'Siege Axe', 'Museum Map']))
    xai_filter.add(Block(theme=decent_unique, comment='Uniques that are usually 2c-1ex', rarity='Unique',
                         base_type=['Onyx Amulet', 'Paua Ring', 'Unset Ring', 'Gold Ring', 'Two-Stone Ring',
                                    'Moonstone Ring', 'Broadhead Arrow Quiver', 'Penetrating Arrow Quiver',
                                    'Spike-Point Arrow Quiver', 'Desert Brigandine', 'Savan', 'Vaal Regalia',
                                    'Full Wyrmscale', 'Varnished Coat', 'Sacrificial Garb', 'Nubuck Boots',
                                    'Sharkskin Boots', 'Slink Boots', 'Conjurer Boots', 'Deerskin Gloves',
                                    'Strapped Mitts', 'Imperial Bow', 'Fiend Dagger', 'Slaughter Knife',
                                    'Imperial Skean', 'Eternal Sword', 'Imperial Staff']))
    xai_filter.add(Block(theme=decent_unique, comment='Unique maps are almost always worth something', rarity='Unique',
                         _class='Maps'))
    # @TODO: add more shit uniques
    xai_filter.add(Block(theme=shit_unique, sockets=Comparer(6, '<'), linked_sockets=Comparer(5, '<'),
                         base_type=['Simple Robe', 'Strapped Boots'], rarity='Unique',
                         comment='Trash Uniques, no sound, same look as normal unique, make sure it has no other special stuff(which we would make sound for) @TODO: add more here'))
    xai_filter.add(Block(theme=unique, rarity='Unique'))

    xai_filter.add(Comment('Section: #0005 - Maps'))
    tier = 16
    for drop_level in range(84, 67, -1):
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

        xai_filter.add(Block(**block_args))
        tier -= 1

    xai_filter.add(Block(theme=gg_fragment, _class='Map Fragments',
                         base_type=['Mortal Hope', 'Mortal Ignorance', 'Fragment of the Phoenix',
                                    'Fragment of the Minotaur', 'Fragment of the Chimera', 'Fragment of the Hydra']))
    xai_filter.add(Block(theme=good_fragment, _class='Map Fragments',
                         base_type=['Mortal', 'Sacrifice at Midnight', 'Eber\'s Key', 'Inya\'s Key', 'Volkuur\'s Key',
                                    'Yriel\'s Key']))
    xai_filter.add(Block(theme=fragment, _class='Map Fragments'))

    xai_filter.add(Comment('Section: #0006 - Currency + Essences'))
    xai_filter.add(Block(theme=gg, base_type=['Exalted Orb', 'Eternal Orb', 'Albino Rhoa Feather']))
    xai_filter.add(Block(theme=good_currency, base_type=['Deafening Essence', 'Shrieking Essence', 'Divine Orb',
                                                         'Unshaping Orb', 'Essence of Hysteria', 'Essence of Insanity',
                                                         'Essence of Horror', 'Essence of Delirium']))
    xai_filter.add(Block(theme=decent_currency,
                         base_type=['Cartographer\'s Sextant', 'Chaos Orb', 'Cartographer\'s Seal', 'Orb of Fusing',
                                    'Orb of Regret', 'Regal Orb', 'Blessed Orb', 'Gemcutter\'s Prism',
                                    'Orb of Scouring', 'Vaal Orb', 'Remnant of Corruption', 'Essence of']))
    xai_filter.add(Block(theme=Theme(text_color=Color(231, 180, 120),
                                     background_color=Color(0, 0, 0, 180),
                                     border_color=Color(231, 180, 120),
                                     font_size=45),
                         base_type='Perandus Coin'))
    xai_filter.add(Block(theme=currency, base_type=['Orb of Alchemy', 'Silver Coin', 'Orb of Chance', 'Jeweller\'s Orb',
                                                    'Orb of Alteration', 'Cartographer\'s Chisel']))
    xai_filter.add(Block(theme=shit_currency, _class=['Currency', 'Stackable Currency']))
    print(xai_filter)

if __name__ == '__main__':
    main()
