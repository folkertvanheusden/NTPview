all:

install:
	mkdir -p $(DESTDIR)$(prefix)/usr/bin
	cp nv.py $(DESTDIR)$(prefix)/usr/bin
	mkdir -p $(DESTDIR)$(prefix)/usr/share/pixmaps
	cp NTPview.xpm $(DESTDIR)$(prefix)/usr/share/pixmaps/NTPview.xpm
	mkdir -p $(DESTDIR)$(prefix)/usr/share/applications
	cp NTPview.desktop $(DESTDIR)$(prefix)/usr/share/applications
