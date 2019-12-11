import pytest
import shlex
import subprocess
import time

containerd_address = 'unix:///run/user/1000/pycontainerd-mock.sock'

@pytest.fixture(scope='module')
def containerd_server():
    command = shlex.split( \
              './containerd_mock.py --address="%s"' % (containerd_address,))
    subprocess.Popen(command)
    time.sleep(1) # give the server time to start up
    return containerd_address

