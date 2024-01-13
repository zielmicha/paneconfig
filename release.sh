#!/bin/bash
set -e
rm -r ~/apps/paneconfig/* || true
rsync -a $(dirname "$0")/ ~/apps/paneconfig/
cd ~/apps/paneconfig
git add .
git diff --cached

git commit -am "release"
