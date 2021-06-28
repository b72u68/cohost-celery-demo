# cohost-celery-demo

A demo website trying to develop a backend with Flask, Celery, and Redis

## Local setup

### Install docker

#### Ubuntu

```
sudo apt install docker
```

#### MacOS

```
brew install docker
```

#### Arch Linux

```
sudo pacman -S docker
```

Visit [Install Docker](https://docs.docker.com/engine/install/) for website
for more information.

### Install docker compose

#### Linux

Install the stable release of Docker compose using `curl`:

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Apply executable permissions to the binary:

```
chmod +x /usr/local/bin/docker-compose
```

Visit [Install docker-compose](https://docs.docker.com/compose/install/) website
for more information.

### Build

```
docker-compose build
```

### Start server

```
docker-compose up

```

### Access

Go to `http://localhost:5000/`.
