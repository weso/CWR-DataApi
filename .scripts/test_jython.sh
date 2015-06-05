#!/bin/bash
# This script runs the tests using Jython

if [ "$JYTHON" == "true" ]; then

   git clone https://github.com/yyuu/pyenv.git ~/.pyenv
   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"

   echo "Installing Jython"
   pyenv install jython-2.7.0
   pyenv local jython-2.7.0

   eval "$(pyenv init -)"

   echo "Interpreter version:"
   python --version

   #wget http://peak.telecommunity.com/dist/ez_setup.py
   #jython ez_setup.py

   #jython ez_install.py yolk

   #jython -m yolk -l

   #jython easy_install.py tox
   #jython easy_install.py pip
   #jython easy_install.py nose

   echo "Running tests"
   #tox -e jython

   #jython -m easy_install pip
   jython -m pip install -rrequirements.txt
   jython -m pip install pytest

   #jython -m easy_install -U pytest
   jython -m py.test

fi
