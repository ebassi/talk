import sys

import gobject
import clutter
import gtk

from talk.core.SlideCollection import SlideCollection
from talk.core.TalkSlide import TalkSlide
from talk.core.TitleSlide import TitleSlide
from talk.core.BulletSlide import BulletSlide
from talk.core.TextSlide import TextSlide

class FosdemTalk:
    TITLE = 'More Clutter'
    SUBTITLE = 'Animating the GNOME platform'

    HEADER = 'more clutter'
    FOOTER = 'FOSDEM 2008 - Bruxelles - Copyright (C) 2008  OpenedHand'

    def __init__ (self):
        self._script = clutter.Script()

        self._collection = SlideCollection()
        self._model = gtk.ListStore(gobject.TYPE_STRING)

        slide = TitleSlide(title=FosdemTalk.TITLE, subtitle=FosdemTalk.SUBTITLE)
        self._collection.set_title_slide(slide)
        self._model.set(self._model.append(), 0, 'Title')

        slide = TextSlide(font='Sans 64px', text='Welcome!')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'welcome')

        items = [ \
          'Emmanuele Bassi', \
          'OpenedHand employee', \
          'Clutter API Grue', \
          'Bindings author/maintainer', \
        ]
        slide = BulletSlide(bullets=items)
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'who am I?')

        slide = TextSlide(font='Sans 48px', text='What is Clutter?')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'what is clutter/1')

        slide = TextSlide(text='Clutter : GNOME = CoreAnimation : OSX')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'what is clutter/2')

        slide_script = '''
{
  "type" : "TextSlide",
  "id" : "orly-slide",
  "text" : "",

  "children" : [
    {
      "type" : "ClutterTexture",
      "id" : "orly",
      "pixbuf" : "data/orly.png",
      "x" : 230,
      "y" : 100,
      "visible" : true
    },
  ]
}
'''
        self._script.load_from_data(slide_script, -1)
        slide = self._script.get_object('orly-slide')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'orly')

        slide = TextSlide(font='Sans 64px', text='YA RLY')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'yarly')

        items = [ \
          'OpenGL 1.1-2.0 / OpenGL-ES 1.1',
          'No matrices',
          'Animations',
          'Nice, friendly, GObject-y C API',
          'Bindings',
          'Integrated with GNOME platform',
        ]
        slide = BulletSlide(bullets=items)
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'what is clutter/3')

        slide = TextSlide(font='Sans 48px', text='2D surfaces in 3D space')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'features/1')

        slide = TextSlide(font='Sans 48px', text='Retained mode')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'features/2')

        slide = TextSlide(font='Sans 48px', text='Properties, not matrices')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'features/3')

        slide = TextSlide(font='Sans 48px', text='Implicit Animations')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'features/4')

        items = [ \
          u'Floating point \u2194 Fixed point', \
          'Subpixel precision', \
          'Cross platform', \
          'GL abstraction', \
        ]
        slide = BulletSlide(bullets=items)
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'features/5')

        slide = TextSlide(font='Sans 56px', text='Clean API')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'in short/1')

        slide = TextSlide(font='Sans 56px', text='+')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'in short/2')

        slide = TextSlide(font='Sans 56px', text='Performance')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'in short/3')

        slide = TextSlide(font='Sans 56px', text='=')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'in short/4')

        slide = TextSlide(font='Sans 128px', text=u'\u2665')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'in short/5')

        slide = TextSlide(font='Sans 42px', text='And if you don\'t like C...')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'bindings/1')

        slide = TextSlide(font='Sans 64px', text='Python')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'bindings/2')

        slide = TextSlide(font='Sans 64px', text='Perl')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'bindings/3')

        slide = TextSlide(font='Sans 64px', text='C++')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'bindings/4')

        slide = TextSlide(font='Sans 64px', text='C#')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'bindings/5')

        slide = TextSlide(font='Sans 64px', text='Vala')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'bindings/6')

        slide = TextSlide(font='Sans 64px', text='Ruby')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'bindings/7')

        slide = TextSlide(font='Sans 42px', text='${INSERT_YOUR_LANGUAGE_HERE}')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'bindings/8')

        slide = TextSlide(font='Sans 48px', text='Clutter 0.6 is out')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'clutter-0-6/1')

        slide = TextSlide(font='Sans 64px', text='Download it <b>NOW</b>\nIt\'s an order')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'clutter-0-6/2')

        slide = TextSlide(font='Sans 48px', text='Questions?')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'q-n-a')

        slide = TextSlide(font='Sans 48px', text='Thank you for listening')
        self._collection.append_slide(slide)
        self._model.set(self._model.append(), 0, 'the end')

    def get_collection (self):
        return self._collection

    def get_model (self):
        return self._model

