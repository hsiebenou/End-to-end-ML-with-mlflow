from pathlib import Path
from mlProject import logger
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation


STAGE_NAME = "Data Transformation stage"


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(":")[-1].strip()
            if status == "True": 
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
        except Exception as e:
            raise e
 
if __name__ == '__main_':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e
