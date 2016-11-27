from block import Block
from filter import Filter


def main():
    simple_filter = Filter()
    simple_filter.add_part(Block(Identified=True, SetTextColor='255 255 0'))
    print(simple_filter)

if __name__ == '__main__':
    main()
