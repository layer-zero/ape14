#! /usr/bin/env bash

rm -rf ape14-samples
curl -L -o master.tar http://github.com/layer-zero/ape14/tarball/master/
tar xvf master.tar
mv layer-zero-ape14-* ape14-samples
rm master.tar

