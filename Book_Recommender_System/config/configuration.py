import os
import sys
from Book_Recommender_System.logger.log import logging
from Book_Recommender_System.exception.exception_handler import AppException
from Book_Recommender_System.utils.utils import read_yaml_file
from Book_Recommender_System.entity.config_entity import DataIngestionConfig
import Book_Recommender_System.constant as constant_module
CONFIG_FILE_PATH = constant_module.CONFIG_FILE_PATH

class AppConfiguration:
    def __init__(self, config_file_path: str = CONFIG_FILE_PATH):
        try:
            self.configs_info = read_yaml_file(file_path = config_file_path)
        except Exception as e:
            raise AppException(e, sys) from e

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            data_ingestion_config_info = self.configs_info['data_ingestion_config']
            artifacts_dir = self.configs_info['artifacts_config']['artifacts_dir']
            dataset_dir = data_ingestion_config_info['dataset_dir']

            ingested_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config_info['ingested_dir'])
            raw_data_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config_info['raw_data_dir'])

            response = DataIngestionConfig(dataset_download_url= data_ingestion_config_info['dataset_download_url'],
                                                        ingested_dir=ingested_dir,
                                                        raw_data_dir=raw_data_dir)
            logging.info(f"Data Ingestion Config: {response}")
            return response
        
        except Exception as e:
            raise AppException(e, sys) from e
