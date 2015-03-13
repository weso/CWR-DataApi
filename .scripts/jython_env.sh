#!/bin/bash
# This script sets up the Jython environment for Travis

if [[ $JYTHON ]]; then

  sudo apt-get install jython
  jython -c "print ''"

fi
