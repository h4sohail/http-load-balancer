# http-load-balancer

An HTTP load balancer implemented in Python

## Goals

- Learn how load balancers work by implementing one myself
- Implement host-based routing
- Implement path-based routing
- Follow test driven development principles

## Commands

```
# build the server image
$ make build

# run the tests
$ make test
```

## Architecture

We use docker-compose to spin up some Flask applications (these could be API servers, or any other resource servers).  
A request arrives at our load balancer that checks the header and/or path to redirect it to the appropriate Flask application.

## Folder Structure

```
├── src
│   ├── app.py - Simple Flask application that will run in each of our servers
│   ├── loadbalancer.py - Load balancer that will distribute traffic to the appropriate server
├── tests
│   ├── test_loadbalancer.py - Unit tests for the load balancer
├── .gitignore
├── Dockerfile - Creates a simple Python image and installs our flask application onto it
├── Makefile - Commands to simplify building and testing the application
├── README.md
├── docker-compose.yml - Starts our HTTP servers for the load balancer
├── requirements.txt
└── .gitignore
```
