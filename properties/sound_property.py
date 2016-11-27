from typing import List

from properties.property import Property


class SoundProperty(Property):
    sound = 1
    volume = 300

    def __init__(self, sound, volume=300):
        self.sound = sound
        self.volume = volume

    def process(self) -> List[str]:
        return ['{0} {1}'.format(self.sound, self.volume)]
