import sys

from talk.core.TalkSlide import TalkSlide
from talk.core.TitleSlide import TitleSlide

class SlideCollection:
    """
    """
    def __init__ (self):
        self.slides = []
        self.cur_slide = 0

    def set_title_slide (self, slide):
        if not isinstance(slide, TitleSlide):
            raise TypeError('slide must be a TitleSlide')
        else:
            self.slides.insert(0, slide)

    def get_title_slide (self):
        return self.slides[0]

    def append_slide (self, slide):
        if not isinstance(slide, TalkSlide):
            raise TypeError('slide must be a TalkSlide')
        else:
            self.slides.append(slide)

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


