#!/bin/bash

# create directory?

# install/download packages required for preprocessing steps (if not done via environment file)

# preprocessing steps for convnext
echo "  preprocessing convnext" 
python -m scripts.preprocessing_convnext data/... data/... # paths to original data and to file where the new data needs to be stored