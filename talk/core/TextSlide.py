import gobject
import pango
import clutter

from talk.core.TalkSlide import TalkSlide

class TextSlide (TalkSlide):
    __gtype_name__ = 'TextSlide'
    __gproperties__ = {
        'title' : (str, 'title', 'title', '', gobject.PARAM_READWRITE),
        'text' : (str, 'text', 'text', '', gobject.PARAM_READWRITE),
    }

    def __init__ (self, title=None, text=None, **kwargs):
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

        self._title = title
        self._title_label = clutter.Label()
        self._title_label.set_color(self.get_text_color())
        self._title_label.set_font_name('Sans 36px')
        self._title_label.set_use_markup(True)
        if self._title:
            self._title_label.set_text(self._title)
        self._title_label.set_width(600)
        self.add(self._title_label)

        x = 50
        y = self.get_header_width() + 50
        self._title_label.set_position(x, y)
        self._title_label.show()

        self._text = text
        self._text_label = clutter.Label()
        self._text_label.set_color(self.get_text_color())
        self._text_label.set_font_name('Sans 28px')
        self._text_label.set_use_markup(True)
        if self._text:
            self._text_label.set_text(self._text)
        self._text_label.set_width(600)
        self.add(self._text_label)

        x = (800 - self._text_label.get_width()) / 2
        y = (600 - self._text_label.get_height()) / 2
        self._text_label.set_alignment(pango.ALIGN_CENTER)
        self._text_label.set_position(x, y)
        self._text_label.show()

    def do_set_property (self, pspec, value):
        if pspec.name == 'title':
            self._title = value
            self._title_label.set_text(self._title)
        elif pspec.name == 'text':
            self._text = value
            self._text_label.set_text(self._text)
        else:
            raise TypeError('Unknown property ' + pspec.name)

    def do_get_property (self, pspec):
        if pspec.name == 'title':
            return self._title
        elif pspec.name == 'text':
            return self._text
        else:
            raise TypeError('Unknown property ' + pspec.name)

gobject.type_register(TextSlide)
