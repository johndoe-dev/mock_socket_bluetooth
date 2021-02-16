import pytest

from tests.fixtures import fixture_host_port
from socket_client import SocketClient


@pytest.fixture()
def host_port():
    return fixture_host_port.fixture_host_port()


@pytest.fixture
def socket_client(host_port):
    socket_client = SocketClient(host_port[0], host_port[1])
    yield socket_client
