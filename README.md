# Mock Socket Bluetooth
App to simulate data of bluetooth
# Development installation
For now we use only built-in module of python


## INSTALLATION

```
$ git clone ssh://git@git.boost.open.global:443/open/recherche_et_developpement/spectrum/mock_socket_bluetooth.git
```

or 

```
$ git clone https://gitlab.boost.open.global/open/recherche_et_developpement/spectrum/mock_socket_bluetooth.git
```

```
$ cd mock_socket_bluetooth
```


## RUN

Example of usage

You have 2 keywords arguments possible in method __start_sending__:
* __number_sending__: 
    * number_sending is the number of time you send data before close connection, it accepts integer, default is -1: create an infinite loop
* __time_laps__:
    * time_laps is the time to wait between each sending (seconds), default is 5

Example in __main.py__

The main is configured to send 5 data with a time laps of 5 seconds

``` python
from socket_client import SocketClient

s = SocketClient('127.0.0.1', 65432)

s.connect()


s.start_sending(5)
```

To run the mock:

``` shell script
$ python main.py
```

## DOCKER

To use, this mock in docker you may use docker __network__ and create container for this project which the __client__ sending fake data and the project [__rpi-communication__](https://gitlab.boost.open.global/open/recherche_et_developpement/spectrum/rpi-communication) which is the __server__ receiving the data

__Make sure to create the both containers (server and client) in 2 differents terminal__

#### Docker network

create a new network with __bridge__ driver

``` shell script
$ docker network create --driver=bridge {network_name}
```

Replace __network_name__ by the name you want for your network

#### Build images


Create the image of the server (rpi-communication):

``` shell script
$ docker build . --tag="{server_name}"
```

Replace __server_name__ by the name you want for your server image


Create the image of the client (this project):

``` shell script
$ docker build . --tag="{client_name}"
```

Replace __client_name__ by the name you want for your server image

#### Run containers

_You need to create the server container before the client container_

Create the server container

``` shell script
docker run  --network={network_name} --name {server_container_name} {server_name}
```

* __network_name__ is the network created above
* __server_container_name__ must match the __HOSTNAME__ define in both Dockerfile of this project and [__rpi-communication__](https://gitlab.boost.open.global/open/recherche_et_developpement/spectrum/rpi-communication).  
The actual value is __ipc_server_dns_name__
* __server_name__ is the name of the server image built above


Create the client container

``` shell script
docker run  --network={network_name} --name {client_container_name} {client_name}
```

* __network_name__ is the network created above
* __client_container_name__ is the container name, you name it whatever you want
* __client_name__ is the name of the client image built above


You can now see the results now in each terminal:

* The client will send data to the server
* The server will receive data from the client

 

#### Example of results

Terminal client:

``` shell script
(venv) ➜  mock_socket_bluetooth git:(master) ✗ docker run  --network=spectrum-bridge --name mock mock-bluetooth              
socket is created
socket is connected
data send: {'mac': '02:00:00:9b:3e:12', 'rssi': '-55'}
data send: {'mac': '02:00:00:33:cd:ba', 'rssi': '-66'}
data send: {'mac': '02:00:00:42:9a:14', 'rssi': '-14'}
data send: {'mac': '02:00:00:80:61:bd', 'rssi': '-79'}
data send: {'mac': '02:00:00:a6:7e:ac', 'rssi': '-87'}
```

Terminal server:

``` shell script
➜  rpi-communication git:(docker) ✗ docker run  --network=spectrum-bridge --name ipc_server_dns_name spectrum-comm

 Reception : waiting to receive message
----DataBody----
mac_address: 02:00:00:9b:3e:12 rssi: ['-55']

----DataBody----
mac_address: 02:00:00:9b:3e:12 rssi: ['-55']
mac_address: 02:00:00:33:cd:ba rssi: ['-66']

----DataBody----
mac_address: 02:00:00:9b:3e:12 rssi: ['-55']
mac_address: 02:00:00:33:cd:ba rssi: ['-66']
mac_address: 02:00:00:42:9a:14 rssi: ['-14']

----DataBody----
mac_address: 02:00:00:9b:3e:12 rssi: ['-55']
mac_address: 02:00:00:33:cd:ba rssi: ['-66']
mac_address: 02:00:00:42:9a:14 rssi: ['-14']
mac_address: 02:00:00:80:61:bd rssi: ['-79']

----DataBody----
mac_address: 02:00:00:9b:3e:12 rssi: ['-55']
mac_address: 02:00:00:33:cd:ba rssi: ['-66']
mac_address: 02:00:00:42:9a:14 rssi: ['-14']
mac_address: 02:00:00:80:61:bd rssi: ['-79']
mac_address: 02:00:00:a6:7e:ac rssi: ['-87']

```


## Test

To run test, you must install __pytest__ and __pytest-cov__

run:

``` shell script
$ pip install pytest pytest-cov
```

or

``` shell script
$ pip install -r requirements.txt
```


Now, to test the project, run:

``` shell script
pytest "tests/"
```

#### Coverage

To run test with coverage:

``` shell script
pytest "tests/" --cov="socket_client" --cov-report html
```

Now  you can open the file __htmlcov/index.html__ in your browser