# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model Developed by Lauren Lee Pope 
This model is a binary classification model, based on the RandomForestClassifier from the scikit-learn repository.   
It can predict whether a persons salary is greater, or equal or less to $50,000 per year based on characteristics like age, education and race.  

## Intended Use
The intended use is to practice building models and pipelines, and will not be used for any additional purposes, or by any other individuals/organizations.  

## Training Data
The  raw data in the census.csv file was sourced from 1994 census data. The raw data was imported into the model, and split into  training and testing datasets in a ratio of 80% training /20% testing.   The data was also encoded using one hot encoder and used the label binarizer method as well.  


## Evaluation Data
The evaluation data is the testing dataset that was split from the original census.csv file. This test data was not used to train the model, but was used to check how well the model performed on data it had not already learned from. The evaluation data was processed using the same one hot encoder and label binarizer that were run on the training data.

## Metrics
The model was evaluated on Precision, Recall and the F1 score.  Across the data slices, precision, recall, and F1 score ranged from 0.0000 to 1.0000. These wide ranges show that the model performed better on some groups than others.
The overall performance scores were:
Precision: 0.7419
Recall: 0.6384
F1 Score: 0.6863 


## Ethical Considerations
If this model were to be used outside of its intended purpose for example to make employment, renting, or other decisions based on any of the categories like race or sex it could lead to decision making bias.  

## Caveats and Recommendations
One caveat to keep in mind is that the data is stale, it is over 30 years old. Because of this, it may not be the best dataset to use if the goal is to gain insight into current earnings patterns based on demographics. I would recommend using a more current dataset if the model were being used for modern analysis.
