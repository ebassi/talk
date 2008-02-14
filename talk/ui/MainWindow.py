import gtk
import gobject
import talk

from os.path import join

class MainWindow (gtk.Window):
    """
    Talk main window.

    This class creates the main window and all the widgets
    needed for a generic presentation.
    """

    def __init__ (self):
        gtk.Window.__init__(self)
        self.set_default_size(800, 600)

if gtk.pygtk_version < (2, 8, 0):
    gobject.type_register(MainWindow)
