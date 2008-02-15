import sys
import gobject
import clutter

class TalkSlide (clutter.Group):
    """
    Base class for slides

    Creates a slide with a header and a footer, fading in/out on show/hide.
    """
    __gtype_name__ = 'TalkSlide'

    WIDTH = 800
    HEIGHT = 600
    PADDING = 5

    def __init__ (self, header=None, footer=None, bg_color=None, text_color=None):
        """
        @param      header: header text
        @type       header: str
        @param      footer: footer text
        @type       footer: str
        @param    bg_color: background color
        @type     bg_color: clutter.Color
        @param  text_color: text color
        @type   text_color: clutter.Color
        """
        clutter.Group.__init__(self)

        self.connect('show', self.on_show)
        self.connect('hide', self.on_hide)

        self._header = header
        if not self._header:
            self._header = 'Unnamed talk'

        self._footer = footer
        if not self._footer:
            self._footer = 'No author, no date'

        self._bg_color = bg_color
        if not self._bg_color:
            self._bg_color = clutter.Color(0, 0, 0, 255)

        self._text_color = text_color
        if not self._text_color:
            self._text_color = clutter.Color(255, 255, 255, 255)

        self._bg_rect = clutter.Rectangle(color=self._bg_color)
        self._bg_rect.set_size(TalkSlide.WIDTH, TalkSlide.HEIGHT)
        self._bg_rect.set_border_width(2)
        self._bg_rect.set_border_color(self._bg_color.lighten())
        self.add(self._bg_rect)
        self._bg_rect.show()

        self._header_label = clutter.Label()
        self._header_label.set_color(self._text_color)
        self._header_label.set_text(self._header)
        self._header_label.set_font_name('Sans 16px')
        self.add(self._header_label)
        self._header_label.set_width(TalkSlide.WIDTH)
        self._header_label.set_position(5, 5)
        self._header_label.set_opacity(0)
        self._header_label.show()

        self._footer_label = clutter.Label()
        self._footer_label.set_color(self._text_color)
        self._footer_label.set_text(self._footer)
        self._footer_label.set_font_name('Sans 12px')
        self.add(self._footer_label)
        self._footer_label.set_position(0, TalkSlide.HEIGHT - self._footer_label.get_height() - 5)
        self._footer_label.set_width(TalkSlide.WIDTH)
        self._footer_label.set_opacity(0)
        self._footer_label.show()

        self._timeline = clutter.Timeline(duration=500)

        self._template = clutter.EffectTemplate(self._timeline, clutter.sine_inc_func)

    def on_show (self, group):
        clutter.effect_fade(self._template, self._header_label, 255)
        clutter.effect_fade(self._template, self._footer_label, 255)

    def on_hide (self, group):
        clutter.effect_fade(self._template, self._header_label, 0)
        clutter.effect_fade(self._template, self._footer_label, 0)

    def get_header_width (self):
        return self._header_label.get_height() + TalkSlide.PADDING

    def get_text_color (self):
        return self._text_color

    def get_bg_color (self):
        return self._bg_color

gobject.type_register(TalkSlide)
