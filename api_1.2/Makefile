PKG = $(shell find dist -name "containerd-*-py3-none-any.whl")

all: dist

build: containerd
	python3 ./setup.py build

dist: build
	python3 ./setup.py bdist_wheel

.PHONY: install test-install
install: $(PKG)
	sudo pip3 install $<

test-install: $(PKG)
	pip3 install $<

.PHONY: uninstall dev_install dev_uninstall
uninstall:
	sudo pip3 uninstall --yes containerd

dev_install:
	sudo pip3 install --editable .

dev_uninstall:
	sudo rm /usr/local/lib/python3.7/dist-packages/containerd.egg-link
	sudo sed -i '/.*\/pycontainerd/d' /usr/local/lib/python3.7/dist-packages/easy-install.pth
	sudo find containerd -uid 0 -exec rm {} \;

.PHONY: clean clobber
clean:
	- rm -r build containerd.egg-info dist

clobber: clean
	- rm -r containerd

