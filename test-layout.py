#!/usr/bin/env python
import clutter
import sys

from os.path import abspath, join, dirname, exists
from optparse import OptionParser

def check_talk_path():
    root_dir = dirname(dirname(__file__))
    if exists(join(root_dir, "Makefile.am")):
        sys.path.insert(0, abspath(root_dir))

check_talk_path()
import talk

from talk.core.TitleSlide import TitleSlide
from talk.core.BulletSlide import BulletSlide
from talk.core.SlideCollection import SlideCollection
from talk.core.TalkLayout import TalkLayout

import gtk

def on_key_press (stage, event):
    if event.keyval == clutter.keysyms.q:
        clutter.main_quit()
        return True

    return False

def build_window():
    stage = clutter.Stage()
    stage.set_size(800, 600)
    stage.set_color(clutter.Color(0, 0, 0, 255))
    stage.connect('key-press-event', on_key_press)
    stage.show()

    collection = SlideCollection()

    title = TitleSlide(title='Test talk')
    collection.set_title_slide(title)

    items = [                                   \
        'first point',                          \
        'second point',                         \
        '<b>third point (kinda important)</b>', \
        '<i>fourth point (optional)</i>',       \
    ]

    slide = BulletSlide(bullets=items, header='test talk')
    collection.append_slide(slide)

    items.append('fifth point')
    slide = BulletSlide(bullets=items, header='test talk')
    collection.append_slide(slide)

    items.append('sixth point')
    slide = BulletSlide(bullets=items, header='test talk')
    collection.append_slide(slide)

    bg = gtk.gdk.pixbuf_new_from_file(join(talk.SHARED_DATA_DIR, 'background.jpg'))
    layout = TalkLayout(collection, bg)
    stage.set_key_focus(layout)

    stage.add(layout)
    layout.set_position(0, 0)
    layout.show()

usage = "talk-clutter [OPTIONS]"
parser = OptionParser(usage=usage)
parser.add_option("-v", "--version", dest="version", action="store_true", help="Print version")
(options, args) = parser.parse_args()

if options.version:
    print talk.defs.VERSION
    sys.exit(0)

build_window()
clutter.main()
