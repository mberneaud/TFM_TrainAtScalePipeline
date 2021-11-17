import os
from math import sqrt

import joblib
import pandas as pd

from google.cloud import storage
from tempfile import TemporaryFile

from sklearn.metrics import mean_absolute_error, mean_squared_error

from TaxiFareModel.params import BUCKET_NAME, MODEL_BUCKET


AWS_BUCKET_TEST_PATH = "s3://wagon-public-datasets/taxi-fare-test.csv"


def get_test_data(nrows, data="s3"):
    """method to get the test data (or a portion of it) from google cloud bucket
    To predict we can either obtain predictions from train data or from test data"""
    # Add Client() here
    path = "data/test.csv"  # ⚠️ to test from actual KAGGLE test set for submission

    if data == "local":
        df = pd.read_csv(path)
    elif data == "full":
        df = pd.read_csv(AWS_BUCKET_TEST_PATH)
    else:
        df = pd.read_csv(AWS_BUCKET_TEST_PATH, nrows=nrows)
    return df


def get_model(path_to_joblib):
    pipeline = joblib.load(path_to_joblib)
    return pipeline


def evaluate_model(y, y_pred):
    MAE = round(mean_absolute_error(y, y_pred), 2)
    RMSE = round(sqrt(mean_squared_error(y, y_pred)), 2)
    res = {'MAE': MAE, 'RMSE': RMSE}
    return res

def download_joblib():
    storage_client = storage.Client()
    bucket_name = BUCKET_NAME
    model_bucket = MODEL_BUCKET

    bucket = storage_client.get_bucket(bucket_name)
    #select bucket file
    blob = bucket.blob(model_bucket)
    with TemporaryFile() as temp_file:
        #download blob into temp file
        blob.download_to_file(temp_file)
        temp_file.seek(0)
        #load into joblib and return
        return joblib.load(temp_file)


def generate_submission_csv(nrows, kaggle_upload=False):
    df_test = get_test_data(nrows)
    pipeline = download_joblib()
    if "best_estimator_" in dir(pipeline):
        y_pred = pipeline.best_estimator_.predict(df_test)
    else:
        y_pred = pipeline.predict(df_test)
    df_test["fare_amount"] = y_pred
    df_sample = df_test[["key", "fare_amount"]]
    name = f"predictions_test_ex.csv"
    df_sample.to_csv(name, index=False)
    print("prediction saved under kaggle format")
    # Set kaggle_upload to False unless you install kaggle cli
    if kaggle_upload:
        kaggle_message_submission = name[:-4]
        command = f'kaggle competitions submit -c new-york-city-taxi-fare-prediction -f {name} -m "{kaggle_message_submission}"'
        os.system(command)


if __name__ == '__main__':

    # ⚠️ in order to push a submission to kaggle you need to use the WHOLE dataset
    nrows = 100
    generate_submission_csv(nrows, kaggle_upload=False)
