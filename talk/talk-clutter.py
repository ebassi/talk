#!/usr/bin/env python
import sys

from os.path import abspath, join, dirname, exists
from optparse import OptionParser

def check_talk_path():
    root_dir = dirname(dirname(__file__))
    if exists(join(root_dir, "Makefile.am")):
        sys.path.insert(0, abspath(root_dir))

check_talk_path()

import gtk

import talk
import talk.defs

from talk.ui.MainWindow import MainWindow

def build_window():
    app = MainWindow()
    app.connect("destroy", gtk.main_quit)
    app.show_all()

    return app

usage = "talk-clutter [OPTIONS]"
parser = OptionParser(usage=usage)
parser.add_option("-v", "--version", dest="version", action="store_true", help="Print version")
(options, args) = parser.parse_args()

if options.version:
    print talk.defs.VERSION
    sys.exit(0)

build_window()
gtk.main()
