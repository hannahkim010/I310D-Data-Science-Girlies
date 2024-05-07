Prior to running any of the notebooks, be sure to change the file directory if importing any of the notebooks to Google Colabs or remove the directory altogether if running locally. However, ensure that the dummy_data.csv file is imported prior to running the file.

In order to run the Linear Regression algorithm, you must have the encoding_module.py file under
the same folder as the notebook for the Linear Regression algorithm. The encoding_module.py file
should include a function used to featurize the training data within the Linear Regression model. Similarily, ensure the same steps were followed prior to running the experimental test case file. 

The neural network does not implement this encoding_module as it uses an alternative encoding technique (that is more automatic and not manually assigned/mapped). Thus, simply following the file directory step and import csv file step should allow the file to compile fully. 
