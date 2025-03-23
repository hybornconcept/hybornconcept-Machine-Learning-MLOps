import sys
import os
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.components.data_ingestion import DataIngestion
from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.data_access.usvisa_data import USvisaData


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifact
        except Exception as e:
            raise USvisaException(e, sys) from e
            
    # def export_data_into_feature_store(self)->DataFrame:
    #     """
    #     Method Name :   export_data_into_feature_store
    #     Description :   This method exports data from mongodb to csv file
        
    #     Output      :   data is returned as artifact of data ingestion components
    #     On Failure  :   Write an exception log and then raise an exception
    #     """
    #     try:
    #         logging.info(f"Exporting data from mongodb")
    #         usvisa_data = USvisaData()
    #         dataframe = usvisa_data.export_collection_as_dataframe(collection_name=
    #                                                               self.data_ingestion_config.collection_name)
    #         logging.info(f"Shape of dataframe: {dataframe.shape}")
    #         feature_store_file_path = self.data_ingestion_config.feature_store_file_path
    #         dir_path = os.path.dirname(feature_store_file_path)
    #         os.makedirs(dir_path,exist_ok=True)
    #         logging.info(f"Saving exported data into feature store file path: {feature_store_file_path}")
    #         dataframe.to_csv(feature_store_file_path,index=False,header=True)
    #         return dataframe
    #     except Exception as e:
    #         raise USvisaException(e,sys) from e
   
    # def split_data_as_train_test(self,dataframe: DataFrame) ->None:
    #     """
    #     Method Name :   split_data_as_train_test
    #     Description :   This method splits the dataframe into train set and test set based on split ratio
        
    #     Output      :   Folder is created in s3 bucket
    #     On Failure  :   Write an exception log and then raise an exception
    #     """
    #     logging.info("Entered split_data_as_train_test method of Data_Ingestion class")
        
    #     try:
    #         train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
    #         logging.info(f"Performed train test split on the dataframe")
    #         logging.info("Exited split_data_as_train_test method of Data_Ingestion class")
            
    #         dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
    #         os.makedirs(dir_path,exist_ok=True)
            
    #         # Additional code to save train and test sets would go here
            
    #     except Exception as e:
    #         raise USvisaException(e,sys) from e
    
    def run_pipeline(self, ) -> None:
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            
            # Additional pipeline stages will be added here
            
        except Exception as e:
            raise USvisaException(e, sys)

   