all: test

.PHONY: prepare-tests test test-docker
prepare clobber clean:

test:
	pytest

docker-test:
		$(MAKE) VERSION=$(VERSION) PYTHON_VERSION=$(PYTHON_VERSION) \
			IMG_NAME=$(IMG_NAME) -C ../infra/docker/tests run

