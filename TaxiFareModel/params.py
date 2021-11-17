MLFLOW_URI = "https://mlflow.lewagon.co/"
EXPERIMENT_NAME = "[GER] [Berlin] [mberneaud] NY Taxi Fare v2"  # 🚨 replace with your country code, city, github_nickname and model name and version

### GCP configuration - - - - - - - - - - - - - - - - - - -

# /!\ you should fill these according to your account

### GCP Project - - - - - - - - - - - - - - - - - - - - - -


### GCP Storage - - - - - - - - - - - - - - - - - - - - - -

BUCKET_NAME = 'wagon-data-735-berneaud'


##### Data  - - - - - - - - - - - - - - - - - - - - - - - -

# train data file location
# /!\ here you need to decide if you are going to train using the provided and uploaded data/train_1k.csv sample file
# or if you want to use the full dataset (you need need to upload it first of course)
BUCKET_TRAIN_DATA_PATH = 'data/train_1k.csv'

GCP_FILE_PATH = f"gs://{BUCKET_NAME}/{BUCKET_TRAIN_DATA_PATH}"


##### Training  - - - - - - - - - - - - - - - - - - - - - -

##### Model - - - - - - - - - - - - - - - - - - - - - - - -

# model folder name (will contain the folders for all trained model versions)

MODEL_NAME = 'taxifare'

# model version folder name (where the trained model.joblib file will be stored)
MODEL_VERSION = 'v2'

# Complete paths to model
PATH_TO_LOCAL_MODEL = 'model.joblib'
MODEL_BUCKET = f"models/{MODEL_NAME}/{MODEL_VERSION}.joblib"
PATH_TO_REMOTE_MODEL = f"gs://{BUCKET_NAME}/models/{MODEL_NAME}/{MODEL_VERSION}.joblib"

### GCP AI Platform - - - - - - - - - - - - - - - - - - - -

# not required here

### - - - - - - - - - - - - - - - - - - - - - - - - - - - -
