from mlProject import logger
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.config.configuration import ConfigurationManager

STAGE_NAME = "Model Evaluation stage"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            raise e
 
if __name__ == '__main_':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e
