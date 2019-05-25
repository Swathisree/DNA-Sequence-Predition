## DNA-Sequence-Prediction
# Sequence classification task: Predicting whether a DNA sequence region is binding site to a specific transcription factor or not
# Transcription factors (TFs) are regulatory proteins that bind specific sequence motifs in the genome to activate or repress transcription of target genes. Genome-wide protein-DNA binding maps can be profiled using some experimental techniques and thus all genomics can be classified into two classes for a TF of interest: bound or unbound
# This program works with three datasets corresponding to three different TFs. 
# The dataset required to run the following project can be found at `https://www.kaggle.com/c/advanced-learning-models-2018` (See the Installation instructions)
## How to get the copy of the project on local machine
# `git clone git@github.com:Swathisree/DNA-Sequence-Predition.git`
## Prerequisites
# You require `Python 3.6`, `Numpy`, `Pandas`, `cvxopt` to run the program. If you do not have the softwares already installed, Follow the instructions below to install the required libraries
## Installation
# Installing libraries:
# sudo apt-get install python3.6
# pip install numpy
# pip install pandas
# pip install cvxopt
# Download datasets:
# Download all files from `https://www.kaggle.com/c/advanced-learning-models-2018/data`
# Save it on same directory of the python scripts 
## Running the scripts
# To run the program using Support Vector Machine: python3 start_svm.py
# To run the program using Logistic Regression: python3 start_LR.py