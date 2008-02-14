import gobject
import clutter

from talk.core.TalkSlide import TalkSlide

class TextSlide (TalkSlide):
    __gtype_name__ = 'TextSlide'

    def __init__ (self, title=None, text=None):
        header = None
        if kwargs.has_key('header'):
            header = kwargs['header']

        footer = None
        if kwargs.has_key('footer'):
            footer = kwargs['footer']

        bg_color = None
        if kwargs.has_key('bg_color'):
            bg_color = kwargs['bg_color']

        text_color = None
        if kwargs.has_key('text_color'):
            bg_color = kwargs['text_color']

        TalkSlide.__init__(self, header, footer, bg_color, text_color)

        self.title = title
        if self.title:
            self._title_label = clutter.Label()
            self._title_label.set_font_name('Sans 36px')
            self._title_label.set_use_markup(True)
            self._title_label.set_text(self.title)
            self._title_label.set_width(600)
            self.add(self._title_label)

            x = 50
            y = self.get_header_width() + 50
            self._title_label.set_position(x, y)
            self._title_label.show()

        self.text = text
        if self.text:
            self._text_label = clutter.Label()
            self._text_label.set_font_name('Sans 28px')
            self._text_label.set_use_markup(True)
            self._text_label.set_text(self.text)
            self._text_label.set_width(600)
            self.add(self._text_label)

            x = 50
            y = self.get_header_width() + 100
            self._text_label.set_position(x, y)
            self._text_label.show()
