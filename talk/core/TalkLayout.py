import gobject
import gtk
import clutter

class TalkLayout (clutter.Group):
    """
    Layout object for the presentation

    TalkLayout is a group arranging the children, taken from
    a SlideCollection, on the Z axis, with decreasing opacity.
    """

    INV_SCALE = 45
    SCALE = 1.0 / INV_SCALE

    def scale_to_depth (self, scale):
        """
        Computes the depth given the scale factor

        @param  scale: scale factor
        @type   scale: float
        """
        actor = clutter.Stage()

        z_camera = actor.get_perspective()[0] # fovy
        z_camera = z_camera * actor.get_width()

        return int((z_camera * scale - z_camera) / scale)

    def __init__ (self, collection=None, background=None):
        """
        Creates a new TalkLayout

        @param  collection: a list of slides
        @type   collection: list of actors or SlideCollection
        @param  background: pixbuf of the background
        @type   background: gtk.gdk.Pixbuf
        """
        clutter.Group.__init__ (self)

        self.collection = collection

        if background and not isinstance(background, gtk.gdk.Pixbuf):
            raise TypeError('background must be either None or a Pixbuf')

        if background:
            self._texture = clutter.Texture(pixbuf=background)
            self._texture.set_opacity(0xaa)
            self.add(self._texture)
            self._texture.set_scale(TalkLayout.INV_SCALE, TalkLayout.INV_SCALE)
            self._texture.set_position(-TalkLayout.INV_SCALE * 800 / 2 + 400,
                                       -TalkLayout.INV_SCALE * 600 / 2 + 300)
            self._texture.set_depth(self.scale_to_depth (TalkLayout.SCALE))
            self._texture.show()
        else:
            self._texture = None

        count = 1
        for slide in self.collection:
            factor = float(count) / float(len(self.collection))

            count = count + 1

            slide.set_opacity(int(255 - (255 * factor)))

            self.add(slide)
            slide.set_position(0, 0)
            slide.set_depth(count * -200)

            slide.show()

