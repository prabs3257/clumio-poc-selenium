#!/bin/bash

docker network create grid-network

docker run -d --name selenium-hub --net grid-network -p 4442-4444:4442-4444 selenium/hub:4.10.0-20230607



