SUBDIRS =
	
talk-clutter: talk-clutter.py
	sed -e "s|\@PYTHONDIR\@|$(pythondir)/talk-clutter|" $< > $@ \
	&& cp $< $(top_srcdir)

talkbindir = $(libdir)/talk-clutter
talkbin_SCRIPTS = talk-clutter

talkdir = $(pythondir)/talk-clutter
talk_PYTHON = \
	defs.py \
	__init__.py
	
BUILT_SOURCES = \
	talk-clutter
	
CLEANFILES = \
	$(BUILT_SOURCES)
	
DISTCLEANFILES = \
	defs.py \
	$(CLEANFILES)
	
EXTRA_DIST = \
	defs.py.in \
	talk-clutter.py
