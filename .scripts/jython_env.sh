#!/bin/bash
# This script sets up the Jython environment for Travis

if [[ $JYTHON ]]; then

  echo "Jython testing active"

  sudo apt-get install jython
  export PYTHON_EXE=jython
  jython -c "print ''"

fi
