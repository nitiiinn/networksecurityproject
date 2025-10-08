import os
import sys
import numpy as np
import pandas as pd

# data ingestion constants 

TARGET_COLUMN="Result"
PIPELINE_NAME="Networksecurity"
ARTIFACTS_DIR="Artifacts"
FILE_NAME="phisingData.csv"

TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"
SCHEMA_FILE_PATH=os.path.join("data_schema","schema.yaml")



DATA_INGESTION_COLLECTION_NAME: str ="NetworkData"
DATA_INGESTION_DATABASE_NAME: str ="STARKK"
DATA_INGESTION_DIR_NAME: str ="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR : str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float =0.2

# DATA VALIDATION RELATED CONSTANTS
DATA_VALIDATION_DIR_NAME: str ="data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"