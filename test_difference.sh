#!/usr/bin/env bash

docker build . --tag minimal_caffe2

docker run --rm -p 8081:8080 --cpus 0.5 --cpuset-cpus 0 --name minimal_caffe2 minimal_caffe2
docker run --rm -p 8081:8080 --cpus 0.5 --cpuset-cpus 0-3 --name minimal_caffe2 minimal_caffe2
