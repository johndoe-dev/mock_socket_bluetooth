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

docker is coming