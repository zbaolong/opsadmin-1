#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from script.client import run

if __name__ == '__main__':
    run()
