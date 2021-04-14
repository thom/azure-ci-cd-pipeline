#!/bin/bash

git clone git@github.com:thom/azure-ci-cd-pipeline.git

cd azure-ci-cd-pipeline

make setup

source ~/.udacity-devops/bin/activate

make all

az webapp up \
    --resource-group flask-ml-service-rg \
    --name flask-ml-service-ikhono \
    --sku F1 \
    --location eastus \
    --verbose
