#!/bin/bash

name=test_calc.py

echo ./${name} -v This uses verbose to show the unit tests as they are being run.


watch "python3 ./${name} -v"
