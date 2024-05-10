import os

import pandas as pd
from sklearn.model_selection import train_test_split

from mlProject import logger
from mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

        ## Note: You can add different data transformation technique
        ## such as Scaler, PCA and all you can perform all kinds of
        ## EDA in ML cycle here before passing this data to the model

        # I amonly adding train_test_spliting cause this data is already cleaned up

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test set (0.75, 0.25) split
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        logger.info("Splited data into training and test sets")
        logger.info(f"train dimension: {train.shape}")
        logger.info(f"test dimension: {test.shape}")
        
