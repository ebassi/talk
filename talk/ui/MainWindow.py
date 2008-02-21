import os
import gobject
import gtk
import gtk.glade
import clutter.cluttergtk

import talk

from talk.core.SlideCollection import SlideCollection
from talk.core.TalkLayout import TalkLayout
from talk.core.TalkSlide import TalkSlide
from talk.core.TitleSlide import TitleSlide
from talk.core.BulletSlide import BulletSlide

from talk.fosdem2008.FosdemTalk import FosdemTalk

from os.path import join

class MainWindow (gtk.Window):
    """
    Talk main window.

    This class creates the main window and all the widgets
    needed for a generic presentation.
    """

    def __init__ (self):
        gtk.Window.__init__ (self)
        self.set_title('Talk')
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_default_size(1024, TalkSlide.HEIGHT)

        self.tree = gtk.glade.XML(join(talk.SHARED_DATA_DIR, 'talk.glade'), root='main_vbox')
        signals = {}
        for attr in dir(self):
            signals[attr] = getattr(self, attr)
        self.tree.signal_autoconnect(signals)

        view_box = self.tree.get_widget('view_box')
        self._embed = clutter.cluttergtk.Embed()
        self._embed.set_flags(gtk.CAN_FOCUS)
        self._embed.set_size_request(TalkSlide.WIDTH, TalkSlide.HEIGHT)
        view_box.pack_end(self._embed, False, False, 0)
        self._embed.show()

        self._main_vbox = self.tree.get_widget('main_vbox')
        self.add(self._main_vbox)
        self.show_all()

        self._menu_bar = self.tree.get_widget('menu_bar')
        self._slides_scroll = self.tree.get_widget('slides_scroll')
        self._status_bar = self.tree.get_widget('status_bar')
        self._tree_view = self.tree.get_widget('slides_view')
        self._fullscreen_menu_item = self.tree.get_widget('fullscreen_menu_item')

        column = gtk.TreeViewColumn('Slides', gtk.CellRendererText(), text=0)
        self._tree_view.append_column(column)

    def on_open_menu_item_activate (self, item):
        pass

    def on_quit_menu_item_activate (self, item):
        gtk.main_quit()

    def on_fullscreen_menu_item_toggled (self, item):
        active = item.get_active()

        if active:
            self._menu_bar.hide()
            self._slides_scroll.hide()
            self._status_bar.hide()
            self.fullscreen()
        else:
            self.unfullscreen()
            self._main_vbox.show_all()

    def on_about_menu_item_activate (self, item):
        pass

    def on_layout_key_press (self, layout, event):
        if event.keyval == clutter.keysyms.f:
            self._fullscreen_menu_item.toggled()
            return True
        elif event.keyval == clutter.keysyms.q:
            gtk.main_quit()
            return True

        return False

    def on_slide_next (self, layout):
        selection = self._tree_view.get_selection()
        (model, iter) = selection.get_selected()
        if not iter:
            iter = model.get_iter_first()
        else:
            iter = model.iter_next(iter)
            if not iter:
                return

        selection.select_iter(iter)
        self._tree_view.scroll_to_cell(model.get_path(iter), None, False,0.0, 0.0)

    def on_slide_prev (self, layout):
        selection = self._tree_view.get_selection()
        (model, iter) = selection.get_selected()
        if not iter:
            iter = model.get_iter_first()
        else:
            index = model.get_path(iter)[0] - 1
            if index < 0:
                selection.unselect_all()
                return
            else:
                iter = model.get_iter((index,))

            if not iter:
                selection.unselect_all()
                return

        selection.select_iter(iter)
        self._tree_view.scroll_to_cell(model.get_path(iter), None, False,0.0, 0.0)

    def build_talk (self):
        stage = self._embed.get_stage()
        stage.set_color(clutter.Color(0, 0, 0, 255))

        current_talk = FosdemTalk()

        collection = current_talk.get_collection()
        model = current_talk.get_model()

        bg = gtk.gdk.pixbuf_new_from_file(join(talk.SHARED_DATA_DIR, 'background.jpg'))
        layout = TalkLayout(collection, bg)
        layout.connect('slide-next', self.on_slide_next)
        layout.connect('slide-prev', self.on_slide_prev)
        layout.connect('key-press-event', self.on_layout_key_press)
        self._tree_view.set_model(model)

        stage.add(layout)
        stage.set_key_focus(layout)
        layout.set_position(0, 0)
        layout.show()

        self._embed.grab_focus()

if gtk.pygtk_version < (2, 8, 0):
    gobject.type_register(MainWindow)
