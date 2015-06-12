#!/bin/bash
# This script deploys the documentation

if [ "$TRAVIS_PULL_REQUEST" == "false" ] && [ "$DEPLOY_DOCS" == "true" ] && [[ "$TRAVIS_BRANCH" == "master" || "$TRAVIS_BRANCH" == "develop" ]]; then

   echo "Deploying docs"
   curl -X POST http://readthedocs.org/build/cwr-dataapi

else

   echo "Docs won't be deployed"

fi