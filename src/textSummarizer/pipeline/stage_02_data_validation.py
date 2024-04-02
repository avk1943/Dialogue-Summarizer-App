from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Initialize the Configuration Manager class
        config = ConfigurationManager()
        # Get data validation configuration from the class
        data_validation_config = config.get_data_validation_config()
        # Call data Validation components
        data_validation = DataValidation(config=data_validation_config)
        # Call the necessary methods
        data_validation.validate_all_files_exist()