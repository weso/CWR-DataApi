#!/bin/bash
# This script deploys the documentation

if [ "$TRAVIS_PULL_REQUEST" == "false" ] && [ "$DEPLOY_DOCS" == "true" ] && [[ "$TRAVIS_BRANCH" == "master" || "$TRAVIS_BRANCH" == "develop" ]]; then

   echo "Deploying docs"
   if [ "$TRAVIS_BRANCH" == "master" ]; then
      curl -X POST http://readthedocs.org/build/cwr-dataapi
   elif [ "$TRAVIS_BRANCH" == "develop" ]; then
      curl -X POST http://readthedocs.org/build/cwr-dataapi/?version=develop
   fi

else

   echo "Docs won't be deployed"

fi