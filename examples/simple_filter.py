from block import Block
from filter import Filter
from properties.color import Color
from properties.sound import Sound
from theme import Theme


def main():
    simple_filter = Filter()

    test_theme = Theme(text_color=Color(255, 255, 0), alert_sound=Sound(5))

    simple_filter.add_part(Block(identified=True, theme=test_theme))
    simple_filter.add_part(Block(show=False, base_type=['Simple Robe']))
    print(simple_filter)

if __name__ == '__main__':
    main()
