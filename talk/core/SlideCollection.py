import sys

from talk.core.TalkSlide import TalkSlide
from talk.core.TitleSlide import TitleSlide

class SlideCollection:
    """
    A collection of slides

    Iterable container. The title slide can only be one, and of
    TitleSlide type.
    """
    def __init__ (self):
        self.slides = []
        self.cur_slide = 0

    def set_title_slide (self, slide):
        if not isinstance(slide, TitleSlide):
            raise TypeError('slide must be a TitleSlide')
        else:
            if self.slides and self.slides[0] is TitleSlide:
                self.slides[0] = None

            self.slides.insert(0, slide)

    def get_title_slide (self):
        if self.slides and self.slides[0] is TitleSlide:
            return self.slides[0]
        else:
            return None

    def append_slide (self, slide):
        if not isinstance(slide, TalkSlide):
            raise TypeError('slide must be a TalkSlide')
        else:
            self.slides.append(slide)

    def append (self, slide):
        if slide is TitleSlide:
            self.set_title_slide(slide)
        else:
            self.append_slide(slide)

    def get_slide (self, index):
        return self.slides[index]

    def __getitem__ (self, key):
        return self.slides[key]

    def __setitem__ (self, key, value):
        if key == 0:
            self.set_title_slide(value)
        else:
            self.slides[key] = value

    def __len__ (self):
        return len(self.slides)

    def __iter__ (self):
        return self

    def next (self):
        if self.cur_slide == len(self.slides):
            raise StopIteration

        item = self.slides[self.cur_slide]
        self.cur_slide = self.cur_slide + 1

        return item

