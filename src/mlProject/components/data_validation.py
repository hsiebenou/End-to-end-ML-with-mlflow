import pandas as pd

from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
from mlProject.utils.common import create_directories


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema
        )
        return data_validation_config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            # validation_status = set(all_cols).issubset(all_schema)
            validation_status = set(all_cols) == set(all_schema)
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"validation status: {validation_status}")

            # for col in all_cols:
            #     if col not in all_schema:
            #         validation_status = False
            #     else:
            #         validation_status = False
            #     with open(self.config.STATUS_FILE, 'w') as f:
            #         f.write(f"validation status: {validation_status}")
            return validation_status
        except Exception as e:
            logger.exception("all columns in data are not the same from schema yaml file")
            raise e