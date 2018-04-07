# Bittrex Bot Tickers


__version__: 0.0.1

Bittrex Bot Tickers is an automate software for gets cryptocurrency tickers
from broker api (Bittrex), then store it, into an embedded database.

The bot use docker container and Ansible script to be deploy.

The platform is developped with python3 (embedded bittrex api), and containe also a mysql container.
All scripts for managing or deploy to a remote host are using Ansible.

> Feel free to improve it or submit your ideas to improve it.

## Summary:

- [Introduction](#introduction)
- [Install](#install)
- [Start](#start)
- [Utils](#utils)
- [Deploy on server](#deploy-on-server)
- [References](#references)


## Introduction

All of these requirements are needed for a local usage.

### Requirements:
- [Python3](https://www.python.org)
- [Docker](https://www.docker.com)
- [Docker-compose](https://docs.docker.com/compose/)
- [Docker network](https://docs.docker.com/network/)

For a server deployment you also need Ansible to be installed and remote hosts available to be managed by Ansible.
### Server Deployment Requirements:
- [Ansible](https://www.ansible.com)
- Remote available for ansible managing

> The server deployment install packages, a list of these packages is available: [here](#ansible-install-packages)


## Install

First at all you must install the bot configuration.
The configuration is a list of cryptocurrency markets store in `config.yml`.

To generate the config file (use python3 script):
```shell
# with make
make install

# if you have any failed with make it's probably because of the python location,
# run the python script manually or make the python3 binary works with
# the command `python3 --version`

python3 config/set_markets_configuration/getMarket.py
```
If this command failed because of missing python3 yaml package install it and retry.

> The python script provide the Bittrex python api wrapper but feel free [to stars the repository](https://github.com/ericsomdahl/python-bittrex).

That will get all available market from Bittrex broker and set into `config.yml`,
You must now set which markets your scroller's will get.

open `docker-compose.yml`:
```yaml
NB_WORKER: 4
BASE_CURRENCY: USDT
...
```
You can set the number of worker the bot will use to get tickers faster.
Workers are  Pool of multiprocess in python3, This is used because of the number
of markets, more longest is the list  more you'll have a long interval time  between tickers.
So, you can split the list market with this number of workers.

In the case above, I want my bot target all market with base currency 'USDT'.

Create a docker network for your automate:
```shell
docker network create websocket-scroller;

# verify with :

docker network ls;
NETWORK ID          NAME                               DRIVER              SCOPE
0db2807c2564        websocket-scroller                 bridge              local
```

## Start

For start the scroller you have to:
```shell
make

# or

make build
make up
```

> take a look at the [Documentation section](#documentation)

## Utils

you can extract the data of your platform by making a dumps.
the makefile provide a command for it:
```shell
make dumps
```
then it generate a mysql-dumps on the root directory  at `backup.sql`.

## Deploy on servers

The project provide on the `server_deploy/` directory a full Ansible script
for being able to make a fast deploy on your servers.

#### little instruction for beginer with ansible

Ansible is a sofware which make the managing of remote server easy, Ansible is an agentless software,
that mean you doesn't need something install on the remote host for using it(except a /bin/python).

The install with ansible will be provide by push ssh.

> Take a look on the Ansible [website](https://www.ansible.com) and [documentation](http://docs.ansible.com/ansible/latest/user_guide/playbooks.html)
> for understand the basic usage of the technologie.

#### set your host configuration.

You must set where you want to deploy, let's open the `server_deploy/inventory` file.

It contain `[scroller]` section, below this section you can add all remote host you want to provide with the script.

```yaml
[scroller]
scroller.servera.com
scroller.serverb.com
scroller.serverc.com
```
You can test if your inventory file can be target by ansible with a ping like :
```shell
$ ansible -m ping scroller
scroller.servera.com | FAILED! => {
    "changed": false,
    "module_stderr": "Shared connection to scroller.servera.com closed.\r\n",
    "module_stdout": "/bin/sh: /usr/bin/python: No such file or directory\r\n",
    "msg": "MODULE FAILURE",
    "rc": 0
}
scroller.serverb.com | FAILED! => {
...
```

If you have the same error you have to install python.

install ansible roles:
```
ansible-galaxy install geerlingguy.docker
```

the script use galaxy role from greerlingguy because his use good practice and
it's easy to use.

> You can found more information about [Ansible Galaxy here](http://docs.ansible.com/ansible/latest/reference_appendices/galaxy.html) and the github of [geerlingguy here](https://github.com/geerlingguy).

Change directory to `server_deploy`:
```
cd server_deploy
```

Next you have to set the location of your bot on your remote hosts:
```
vi inventory;
...
[scroller:vars]
scroller_path=/path/to/your/bot/tickerBot/
```

Before runing script you have to know what it does:
1. install docker with the external role from geerlingguy
2. install python3 and python3-pip + upgrade pip
3. clone the platform repository, then make it 2 time one for init mysql, seconde for run bot.

Run script:
```
ansible-playbook deploy_bot.yml  -K
```
The option -K is for the packages installation, the script need the root permission to run package manager,
so the -K option ask what is the sudo password.(its possible to specifying in the hosts file, take a
look at the Ansible documentation)


for get the sql dump you have to connect to your remote hosts for run the command `make dumps`,
then use scp to get it locally.

## logs
you can verify your module is up with:
```shell
  make ps
```

for logs:
```shell
  # all logs
  make logs
```

## Documentation

_Makefile commands available_:

| **commands name** | **description**              |
|:-----------------:|:---------------------------- |
|      `make`       | 1. down each service         |
|                   | 2. build basic project       |
|                   | 3. run project               |
|                   |                              |
|  `make build_up`  | 1. build basic project       |
|                   | 2. run project               |
|                   |                              |
|   `make build`    | build basic project.         |
|                   |                              |
|     `make up`     | run project                  |
|                   |                              |
|    `make down`    | down project                 |
|                   |                              |
|     `make ps`     | list container               |
|                   |                              |
|   `make dumps`    | make a sql dumps of tickers. |
|                   |                              |
|    `make logs`    | display all logs             |

_Tricks_:

|              **commands**              | **description**         |
|:--------------------------------------:|:----------------------- |
| `docker network create "Network-Name"` | Create a docker network |
|          `docker network ls`           | List docker network     |

_Troubles possible_:

make logs failed:
if the commands failed use the docker-compose command:
`docker-compose logs -f`

## Reference


> - [Mysql compose hub](https://hub.docker.com/_/mysql/)
> - [Mysql documentation](https://dev.mysql.com/doc/)
> - [Docker website](https://www.docker.com)
> - [Docker-compose documentation](https://docs.docker.com/compose/)
> - [Git documentation](https://git-scm.com/documentation)
> - [Docker network documentation](https://docs.docker.com/engine/userguide/networking/work-with-networks/)

### Ansible install packages

- docker
- docker-compose
- websocket-scroller (by github clonging)

## version

| **Version** | **Description**                                       |
|:-----------:|:----------------------------------------------------- |
|    0.0.1    | automate get ticker rest multiprocess + embedded mysql container |                                           |
