# Makefile for the Python project
#
# It supports creating distribution files, and deploying them to Pypi and Pypitest or installing them locally
#
# A Python interpreter is required, and it should be accessible from the command line.
 
# Sets the variables.
 
# Sets the Python executable.
# It will be the executable for the interpreter set up for the command line.
PYTHON   = python
 
# Sets the distribution folder.
# It will be the 'dist' folder.
DISTDIR   = dist
 
# Sets the .egg file path.
# The file will be located at the project's root.
EGGDIR    = CWR_API.egg-info

# Sets the tox folder path.
# It will be the '.tox' folder.
TOXDIR    = .tox
 
# User-friendly check for sphinx-build
ifeq ($(shell which $(PYTHON) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(PYTHON)' command was not found. Make sure you have a version of the python interpreter installed, then add the directory where it was installed to the PATH.)
endif
 
.PHONY: help clean 
 
# Help option
# Shows the allowed commands to be received as parameters
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  dist_source    to make the standard distribution"
	@echo "  dist_binary    to make the binary distribution"
	@echo "  install        to install the project"
	@echo "  pypi_reg       to register on pypi"
	@echo "  pypitest_reg   to register on testpypi"
	@echo "  pypi           to upload to pypi"
	@echo "  pypitest       to upload to testpypi"
	@echo "  test           to run tests"

# Clean option
# Removes the distribution folder and the .egg file
clean:
	rm -r -f $(DISTDIR)
	rm -r -f $(EGGDIR)
	rm -r -f $(TOXDIR)

# Source distribution.
dist_source:
	$(PYTHON) setup.py sdist

# Binary distribution.
dist_binary:
	$(PYTHON) setup.py bdist

# Install in local libraries repository
install:
	$(PYTHON) setup.py install
 
# Pypi registration.
pypi_reg:
	$(PYTHON) setup.py register -r pypi
 
# Pypitest registration.
pypitest_reg:
	$(PYTHON) setup.py register -r testpypi
 
# Pypi deployment.
pypi:
	$(PYTHON) setup.py sdist upload -r pypi
 
# Pypitest deployment.
pypitest:
	$(PYTHON) setup.py sdist upload -r testpypi

# Tests suite.
test:
	tox
