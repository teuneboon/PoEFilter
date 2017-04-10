from block import Block
from comment import Comment
from filter import Filter
from helpers.colors import Colors
from helpers.general import add_failsafe
from properties.color import Color
from properties.comparer import Comparer
from properties.sound import Sound
from theme import Theme


def main():
    f = Filter()
    t = themes()

    f.add(Comment('Section: #001 - Special Stuff\n'))
    f.add(Block(theme=t['lab_and_shaper_orb'], _class='Quest Items', base_type='Shaper\'s Orb'))
    f.add(Block(theme=t['lab_and_shaper_orb'], base_type='Offering to the Goddess'))
    f.add(Block(theme=t['quest'], _class=['Quest Items', 'Microtransactions', 'Hideout Doodads']))
    f.add(Block(theme=t['quest'], _class='Labyrinth', play_alert_sound=Sound(1)))
    f.add(Block(theme=t['t0'], item_level=1, rarity='Normal',
                base_type=['Glass Shank', 'Driftwood Wand', 'Rusted Sword', 'Crude Bow', 'Driftwood Sceptre'],
                play_alert_sound=None,
                comment='Make ilvl 1 of starter weapons ugly so people know they forgot their racing filter @TODO: add others'))

    f.add(Comment('Section: #002 - GG!!!\n'))
    f.add(Block(theme=t['t0'], base_type=['Mirror of Kalandra', 'Fishing Rod']))
    f.add(Block(theme=t['t0'], linked_sockets=Comparer(6, '>=')))

    f.add(Comment('Section: #014 - Failsafe\n'))
    add_failsafe(f)

    with open('Xai.filter', encoding='utf-8', mode='w') as file:
        file.write(str(f))


def themes():
    t0_highlight = Colors.BLOOD_RED
    t0_background = Colors.WHITE

    t1_highlight = Color(0, 93, 255)
    t2_highlight = Color(153, 255, 0)
    t3_highlight = Color(50, 0, 117)
    break_1 = Color(255, 230, 122)
    break_2 = Color(122, 255, 148)
    breach = Color(65, 20, 80)

    return {
        'lab_and_shaper_orb': Theme(text_color=t1_highlight, background_color=break_1, border_color=t1_highlight, font_size=45, alert_sound=1),
        'quest': Theme(text_color=break_2, border_color=break_2, font_size=45, alert_sound=1),
        't0': Theme(text_color=t0_highlight, border_color=t0_highlight, background_color=t0_background, font_size=45, alert_sound=8)
    }

if __name__ == '__main__':
    main()
