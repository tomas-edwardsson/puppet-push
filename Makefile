NAME=puppet-push
VERSION=0.1
 
DOC_FILES=README.md LICENSE etc/site-push.pp-example
 
PKG_DIR=pkg
PKG_NAME=$(NAME)-$(VERSION)
PKG=$(PKG_DIR)/$(PKG_NAME).tar.gz
SIG=$(PKG_DIR)/$(PKG_NAME).asc

# Hack, since RHEL6 git doesn't know how to .tar.gz archives.
TARPKG=$(PKG_DIR)/$(PKG_NAME).tar
 
PREFIX?=/usr
DOC_DIR=$(PREFIX)/share/doc/$(PKG_NAME)
BINDIR=$(PREFIX)/bin
ifeq ($(PREFIX), /usr)
SYSCONFDIR=/etc
else
SYSCONFDIR=$(PREFIX)/etc
endif
LIBEXECDIR=$(PREFIX)/libexec/puppet-push
SHAREDSTATEDIR=/var/lib/$(NAME)
 
pkg:
	mkdir -p $(PKG_DIR)
 
$(PKG): pkg
	git archive --format=tar --output=$(TARPKG) --prefix=$(PKG_NAME)/ HEAD
	gzip $(TARPKG)
 
build: $(PKG)
 
$(SIG): $(PKG)
	gpg --sign --detach-sign --armor $(PKG)
 
sign: $(SIG)
 
clean:
	rm -f $(PKG) $(SIG)
 
all: $(PKG) $(SIG)
 
test:
 
install:
	install -D -m 755 -o root -g root bin/puppet-push $(BINDIR)/puppet-push
	install -D -m 755 -o root -g root bin/extract-file-sources.py $(LIBEXECDIR)/extract-file-sources.py
	install -D -m 755 -o root -g root -b etc/puppet-push.conf $(SYSCONFDIR)/puppet-push.conf
	for docfile in $(DOC_FILES); do install -D -m 755 -o root -g root $$docfile $(DOC_DIR)/$$docfile; done
	mkdir -p $(SHAREDSTATEDIR)
 
uninstall:
	rm $(BINDIR)/puppet-push
	rm $(LIBEXECDIR)/extract-file-sources.py
	rm $(SYSCONFDIR)/puppet-push.conf
	test "x$(DOC_DIR)" != "x" && rm -rf $(DOC_DIR)
	test "x$(SHAREDSTATEDIR)" != "x" && rm -rf $(SHAREDSTATEDIR)

rpm: $(PKG)
	rpmbuild -tb $(PKG)
 
.PHONY: build sign clean test install uninstall all rpm
