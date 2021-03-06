#!/usr/bin/env bash

docker build . --tag minimal_caffe2

echo "Pinned to one core:"
docker run --rm --cpuset-cpus 0 --name minimal_caffe2 minimal_caffe2
echo "Pinned to four cores:"
docker run --rm --cpuset-cpus 0-3 --name minimal_caffe2 minimal_caffe2
