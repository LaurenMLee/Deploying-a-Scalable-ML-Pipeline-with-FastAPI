import pytest
# TODO: add necessary import
import pandas as pd
from sklearn.model_selection import train_test_split
from ml.model import compute_model_metrics,save_model,train_model
import os

# TODO: implement the first test. Change the function name and input as needed

def test_data_split_ratio():
    """
    # add description for the first test
   
    This test confirms that the data split occurs in an 80% training/ 20% testing ratio
    """ 
    # Your code here
    data = pd.read_csv("data/census.csv")

    train, test = train_test_split(data, test_size=0.20, random_state=42)

    total_rows = len(data)
    train_ratio = round(len(train)/total_rows,1)
    test_ratio = round(len(test)/total_rows,1)

    assert train_ratio == 0.8
    assert test_ratio == 0.2


# TODO: implement the second test. Change the function name and input as needed
def test_all_metrics_returned():
    """
    # add description for the second test

    This test confirms that all three metrics are returned, Precision, Recall and F1 score
    """
    # Your code here
    y = [1,0,1,1,0,1,1,1]
    preds = [1,1,0,0,1,1,0,0]

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1






# TODO: implement the third test. Change the function name and input as needed
def test_model_saved(tmp_path):

    """
    # add description for the third test

    This test confims that the model is saved successfully.
    """
    # Your code here
    x_train = [[1,0],[1,1],[0,1,],[0,0]]
    y_train = [1,0,1,0]

    model = train_model(x_train,y_train)
    file_path =  tmp_path / "modeltest.pkl"
    save_model (model,file_path)

    assert file_path.exists()
    assert file_path.stat().st_size > 0
