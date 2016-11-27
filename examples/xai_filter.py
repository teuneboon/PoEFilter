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

    xai_filter.add(Comment('Section: #0001 - Special Stuff\n'))
    xai_filter.add(Block(theme=decent_unique,
                         comment='Tabula, we have to put this before everything cause our 6L block will override otherwise',
                         socket_group='WWWWWW',
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


    print(xai_filter)

if __name__ == '__main__':
    main()
