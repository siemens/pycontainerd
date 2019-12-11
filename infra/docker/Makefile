VERSION?=1.2.1
PYTHON_VERSION?=3.7
SUBDIRS=tests build

export

push prepare clobber clean:
	for dir in $(SUBDIRS) ; do $(MAKE) -C $$dir $@ ; done

