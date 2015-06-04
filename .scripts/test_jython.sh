#!/bin/bash
# This script runs the tests using Jython

if [ "$JYTHON" == "true" ]; then

   git clone https://github.com/yyuu/pyenv.git ~/.pyenv
   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"
   pyenv install pypy-2.5.0
   mkdir ~/jython_test
   cd ~/jython_test
   pyenv global pypy-2.5.0

   eval "$(pyenv init -)"

   python --version

   pip install tox

   tox -e jython

fi
