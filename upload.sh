#!/bin/bash
rm -rf dist
python3 -m pip install --upgrade pip setuptools wheel twine
python3 setup.py sdist
python3 -m twine upload dist/*
