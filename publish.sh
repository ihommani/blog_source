#! /bin/sh

set -e

pelican content -o output -s publishconf.py
ghp-import output
git push git@github.com:ihommani/ihommani.github.io.git gh-pages:master

