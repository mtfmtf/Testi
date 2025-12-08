#!/bin/bash

docker run -it --rm \
  -p 4000:4000 \
  -v "$PWD":/usr/src/app \
  starefossen/github-pages
