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
                          font_size=45, alert_sound=Sound(6))
    special_quest_item = Theme(text_color=Colors.WHITE, background_color=Color(0, 128, 0), font_size=45,
                               alert_sound=Sound(1))
    quest_item = Theme(text_color=Color(50, 230, 100), border_color=Color(74, 230, 58), font_size=45)
    gg = Theme(text_color=Color(210, 0, 220), background_color=Colors.WHITE, border_color=Color(208, 32, 144),
               font_size=45, alert_sound=Sound(8))

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

    print(xai_filter)

if __name__ == '__main__':
    main()
