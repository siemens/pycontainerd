VERSION?=1.2.0
PYTHON_VERSION?=3.7
SUBDIRS=docker

export

prepare clobber clean:
	for dir in $(SUBDIRS) ; do $(MAKE) -C $$dir $@ ; done

