from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Initialize the Configuration Manager class
        config = ConfigurationManager()
        # Get data transformation configuration from the class
        data_transformation_config = config.get_data_transformation_config()
        # Call data transformation components
        data_transformation = DataTransformation(config=data_transformation_config)
        # Call the necessary methods
        data_transformation.convert()