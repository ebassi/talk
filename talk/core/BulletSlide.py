import sys
import gobject
import clutter

from talk.core.TalkSlide import TalkSlide

class BulletSlide (TalkSlide):
    __gtype_name__ = 'BulletSlide'

    def __init__ (self, title=None, bullets=None, **kwargs):
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

        self.bullets = []
        if bullets and len(bullets) > 0:
            self.bullets = bullets

        count = 1
        for bullet in self.bullets:
            text = u'\u2023 ' + bullet

            label = clutter.Label()
            label.set_color(clutter.Color(255, 255, 255, 255))
            label.set_font_name('Sans 28px')
            label.set_use_markup(True)
            label.set_text(text)
            label.set_width(600)
            self.add(label)

            x = 50
            y = self.get_header_width() + (count * 50) + 100

            label.set_position(x, y)
            label.show()

            #print "bullet[%d] = '%s' (%d, %d)" % (count, text, x, y)

            count = count + 1

