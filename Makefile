LAST_RELEASE=$(shell script/get_version.bash -r)
VERSION=$(shell script/get_version.bash)
PYTHON_VERSION?=3.7
IMG_NAME_PR?=docker.pkg.github.com/siemens/pycontainerd/pycontainerd
SUBDIRS=script tests infra
SUPPORTED_APIS=1.2 1.3
API_DIRS=$(addprefix api_,$(SUPPORTED_APIS))

export

.PHONY: all
all: package

version:
	@echo Last release: $(LAST_RELEASE)
	@echo Version: $(VERSION)

.PHONY: stubs
stubs:
	@ for api in $(SUPPORTED_APIS); do $(MAKE) api_$$api ; done

api_%: script/genpb2.sh resources/containerd/__init__.py.in resources/containerd/services/events/v1/__init__.py
	./script/genpb2.sh -a $*
	cp resources/api_Makefile $@/Makefile

.PHONY: packages test docker-test
packages: $(API_DIRS)
	@ for api in $(API_DIRS) ; do $(MAKE) -C $$api dist ; done
	mkdir -p $@
	@ for api in $(API_DIRS) ; do cp $$api/dist/* $@ ; done

test:
	$(MAKE) -C tests test

prepare:
	for dir in $(SUBDIRS) ; do $(MAKE) -C $$dir $@ ; done

docker-test: package prepare
	$(MAKE) -C tests $@

push-docker:
	$(MAKE) -C infra/docker push

.PHONY: clean clobber
clean:
	- for api in $(API_DIRS) ; do $(MAKE) -C $$api $@ ; done
	- for dir in $(SUBDIRS) ; do $(MAKE) -C $$dir $@ ; done
	- rm -r build containerd.egg-info dist

clobber: clean
	- for dir in $(SUBDIRS) ; do $(MAKE) -C $$dir $@ ; done
	- for api in $(API_DIRS) ; do rm -r $$api ; done

