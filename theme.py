from properties.sound import Sound


class Theme(object):
    text_color = None
    border_color = None
    background_color = None
    font_size = None
    alert_sound = None

    def __init__(self, text_color=None, border_color=None, background_color=None, font_size=None, alert_sound=None):
        self.text_color = text_color
        self.border_color = border_color
        self.background_color = background_color
        self.font_size = font_size
        if isinstance(alert_sound, int):
            alert_sound = Sound(alert_sound)
        self.alert_sound = alert_sound

    def process(self, block):
        block.set_property('set_text_color', self.text_color)
        block.set_property('set_border_color', self.border_color)
        block.set_property('set_background_color', self.background_color)
        block.set_property('set_font_size', self.font_size)
        block.set_property('play_alert_sound', self.alert_sound)
