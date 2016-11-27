from block import Block
from comment import Comment
from filter import Filter
from helpers.colors import Colors
from properties.color import Color
from properties.sound import Sound
from theme import Theme


def main():
    xai_filter = Filter()

    decent_unique = Theme(text_color=Colors.WHITE, background_color=Colors.UNIQUE, border_color=Colors.WHITE,
                          font_size=45, alert_sound=Sound(6))
    special_quest_item = Theme(text_color=Colors.WHITE, background_color=Color(0, 128, 0), font_size=45,
                               alert_sound=Sound(1))
    quest_item = Theme(text_color=Color(50, 230, 100), border_color=Color(74, 230, 58), font_size=45)

    xai_filter.add(Comment('Section: #0001 - Special Stuff'))
    xai_filter.add(Block(theme=decent_unique,
                         comment='Tabula, we have to put this before everything cause our 6L block will override otherwise',
                         socket_group='WWWWWW',
                         rarity='Unique'))
    xai_filter.add(Block(theme=special_quest_item, _class='Quest Items', base_type='Shaper\'s Orb'))
    xai_filter.add(Block(theme=quest_item, _class=['Quest Items', 'Microtransactions']))

    print(xai_filter)

if __name__ == '__main__':
    main()
