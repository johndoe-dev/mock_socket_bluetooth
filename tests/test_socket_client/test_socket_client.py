from unittest import mock
from socket_client import generate_data


def test_generate_data():
    data = generate_data()
    assert isinstance(data['mac'], str)
    assert isinstance(data['rssi'], str)


class TestSocketClient:

    def test_connect(self, socket_client):
        with mock.patch('socket.socket'):
            # mock_socket.return_value.recv.return_value = "test"
            socket_client.connect()

        socket_client.socket.connect.assert_called_with(("", 1234))

    def test_connect_failed(self, socket_client):
        connected = socket_client.connect()
        assert not connected

    def test_start_sending_ok(self, socket_client):
        with mock.patch('socket.socket') as mock_socket:
            socket_client.connect()
            response = socket_client.start_sending(2, 1)
            mock_socket.return_value.recv.return_value = "test"

        assert response["status"]
        assert response["message"] == "2 data send"

    def test_start_sending_fail(self, socket_client):
        with mock.patch('socket.socket') as mock_socket:
            response = socket_client.start_sending(2, 1)
            mock_socket.return_value.recv.return_value = "test"

        assert not response["status"]
        assert response["message"] == "Make sure to call connect() before"
