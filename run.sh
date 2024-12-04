#!/bin/bash

MAIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

source $MAIN_DIR/env/bin/activate; python3 $MAIN_DIR/src/main.py
