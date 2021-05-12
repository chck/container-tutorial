#!/bin/bash
#
# ref: https://gist.github.com/g105b/34ec96a305b74087d5a64db27d1b9fec
#
target=${1:-http://0.0.0.0:8000}
while true
do
  curl $target && echo
done
