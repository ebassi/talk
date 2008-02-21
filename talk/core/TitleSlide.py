import sys
import gobject
import clutter

from talk.core.TalkSlide import TalkSlide

class TitleSlide (TalkSlide):
    __gtype_name__ = 'TitleSlide'

    def __init__ (self, title=None, subtitle=None, author=None, **kwargs):
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
            text_color = kwargs['text_color']

        TalkSlide.__init__(self, header, footer, bg_color, text_color)

        if not title:
            title = 'Unnamed talk'

        if not subtitle:
            subtitle = 'Insert witty subtitle here'

        if not author:
            author = 'Insert your name here'

        self._title_label = clutter.Label()
        self._title_label.set_font_name('Sans 64px')
        self._title_label.set_color(clutter.Color(255, 255, 255, 255))
        self._title_label.set_text(title)
        self.add(self._title_label)
        self._title_label.set_anchor_point(self._title_label.get_width() / 2,
                                           self._title_label.get_height() / 2)
        self._title_label.set_position(TalkSlide.WIDTH / 2,
                                       TalkSlide.HEIGHT / 2)
        self._title_label.show()

        self._subtitle_label = clutter.Label()
        self._subtitle_label.set_font_name('Sans 32px')
        self._subtitle_label.set_color(clutter.Color(255, 255, 255, 255))
        self._subtitle_label.set_text(subtitle)
        self.add(self._subtitle_label)
        self._subtitle_label.set_anchor_point(self._subtitle_label.get_width() / 2,
                                              self._subtitle_label.get_height() / 2)
        self._subtitle_label.set_position(TalkSlide.WIDTH / 2,
                                          TalkSlide.HEIGHT / 2 
                                          + self._title_label.get_height()
                                          + 10)
        self._subtitle_label.show()

        self._author_label = clutter.Label()
        self._author_label.set_font_name('Sans 24px')
        self._author_label.set_color(clutter.Color(255, 255, 255, 255))
        self._author_label.set_text(author)
        self.add(self._author_label)
        self._author_label.set_anchor_point(self._author_label.get_width() / 2,
                                            self._author_label.get_height() / 2)
        self._author_label.set_position(TalkSlide.WIDTH / 2,
                                        TalkSlide.HEIGHT / 2 
                                        + self._title_label.get_height()
                                        + self._subtitle_label.get_height()
                                        + 10)
        self._author_label.show()

