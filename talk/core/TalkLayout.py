import gobject
import gtk
import clutter

class TalkLayout (clutter.Group):
    """
    Layout object for the presentation

    TalkLayout is a group arranging the children, taken from
    a SlideCollection, on the Z axis, with decreasing opacity.
    """
    __gsignals__ = {
      'slide-next' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, ()),
      'slide-prev' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, ()),
    }

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
        self.set_reactive(True)
        self.connect('key-press-event', self.on_key_press)

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

        count = 0
        for slide in self.collection:
            factor = float(count + 1) / float(len(self.collection))

            slide.set_opacity(int(255 - (255 * factor)))

            self.add(slide)
            slide.set_position(0, 0)
            slide.set_depth((count + 1) * -200)

            slide.show()

            count = count + 1


        self.current_index = 0

        timeline = clutter.Timeline(duration=250)
        self._template = clutter.EffectTemplate(timeline, clutter.sine_inc_func)

    def on_depth_complete (self, group, direction):
        if (self.current_index - 1) < 0:
            return

        self.collection[self.current_index - 1].emit('slide-visible')

    def on_key_press (self, group, event):
        if not self.collection:
            return False

        current = self.current_index
        try:
            slide = self.collection[current]
        except Exception, ex:
            slide = None

        if event.keyval == clutter.keysyms.k:
            next = current + 1
            direction = 'forward'
        elif event.keyval == clutter.keysyms.j:
            next = current - 1
            direction = 'backward'
        else:
            return False

        if next < 0 or next > len(self.collection):
            return False

        depth = next * -200

        try:
            next_slide = self.collection[next]
        except Exception, ex:
            next_slide = None

        # we start with the title slide at a non-zero depth, so
        # we need to special-case it
        if current == 0:
            clutter.effect_fade(self._template, slide, 255)
        elif next == 0:
            opacity = float(next + 1) / float(len(self.collection))
            opacity = int(255 - (255 * opacity))
            clutter.effect_fade(self._template, next_slide, opacity)
        else:
            prev_slide = self.collection[current - 1]

            if direction == 'forward':
                clutter.effect_fade(self._template, prev_slide, 0)
                if slide:
                    clutter.effect_fade(self._template, slide, 255)
            else:
                opacity = float(current) / float(len(self.collection))
                opacity = int(255 - (255 * opacity))
                clutter.effect_fade(self._template, prev_slide, opacity)
                if next_slide:
                    clutter.effect_fade(self._template, next_slide, 255)

        if direction == 'forward':
            self.emit('slide-next')
        else:
            self.emit('slide-prev')

        # move the group to the next slide's depth
        clutter.effect_depth(self._template, self, -depth,
                             self.on_depth_complete,
                             direction)

        self.current_index = next
