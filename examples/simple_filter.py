from block import Block
from filter import Filter
from properties.color_property import ColorProperty
from properties.sound_property import SoundProperty
from theme import Theme


def main():
    simple_filter = Filter()

    test_theme = Theme(text_color=ColorProperty(255, 255, 0), alert_sound=SoundProperty(5))

    simple_filter.add_part(Block(identified=True, theme=test_theme))
    simple_filter.add_part(Block(show=False, base_type='Simple Robe'))
    print(simple_filter)

if __name__ == '__main__':
    main()
