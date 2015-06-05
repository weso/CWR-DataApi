#!/bin/bash
# This script runs the tests using Jython

if [ "$JYTHON" == "true" ]; then

   git clone https://github.com/yyuu/pyenv.git ~/.pyenv
   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"

   echo "Installing Jython"
   pyenv install jython-2.7.0
   pyenv global jython-2.7.0

   eval "$(pyenv init -)"

   echo "Interpreter version:"
   python --version

   echo "pip version:"

   jython -m --version

   jython -m install tox

   echo "Running tests"
   #tox -e jython

   jython -m pip install -rrequirements.txt
   jython -m pip install nose
   jython nosetests

fi
