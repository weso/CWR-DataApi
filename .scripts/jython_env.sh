#!/bin/bash
# This script sets up the Jython environment for Travis

if [[ $TOXENV == "jython"* ]]; then

  source ~/virtualenv/python2.7/bin/activate
  sudo apt-get install jython
  export PYTHON_EXE=jython; jython -c "print ''"

fi
