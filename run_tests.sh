#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/test_flaskr.py -v