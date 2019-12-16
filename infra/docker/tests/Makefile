VERSION?=1.2.1
PYTHON_VERSION?=3.7
IMG_NAME=${IMG_NAME_PR}/test:$(VERSION)

export

.PHONY: all prepare run push clean clobber

all: prepare

Dockerfile: Dockerfile.in
	env PYTHON_VERSION=$(PYTHON_VERSION) \
		envsubst '$${PYTHON_VERSION}' \
		< Dockerfile.in > Dockerfile

prepare: Dockerfile
	docker image build -t $(IMG_NAME) .
	rm Dockerfile

run:
	docker container run --rm \
		--volume=$$(pwd)/../../../dist:/pycontainerd \
		--volume=$$(pwd)/../../../tests:/tests \
		${IMG_NAME} \
		bash -c 'pip3 install /pycontainerd/containerd-$(VERSION)-py3-none-any.whl ; pytest'

push:
	docker push ${IMG_NAME}

clean:
	- rm Dockerfile

clobber: clean
	- docker image rm $(IMG_NAME)

