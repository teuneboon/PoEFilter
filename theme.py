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
        self.alert_sound = alert_sound

    def process(self, properties):
        if self.text_color is not None:
            properties['SetTextColor'] = self.text_color
        if self.border_color is not None:
            properties['SetBorderColor'] = self.border_color
        if self.background_color is not None:
            properties['SetBackgroundColor'] = self.background_color
        if self.font_size is not None:
            properties['SetFontSize'] = self.font_size
        if self.alert_sound is not None:
            properties['PlayAlertSound'] = self.alert_sound
