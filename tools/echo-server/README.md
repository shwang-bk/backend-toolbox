# echo-server
The simplest request echo server

## Requirement
pipenv

## Installation
```sh
$ git clone https://github.com/shwang-bk/echo-server
$ cd echo-server
$ pipenv install
```

## Usage
```sh
pipenv run uvicorn echo:app --host 0.0.0.0 --port 8000
```