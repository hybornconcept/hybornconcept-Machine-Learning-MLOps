import sys
import pandas as pd
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.configuration.mongo_db_connection import MongoDBClient

class USvisaData:
    """
    This class helps to export entire mongodb record as pandas dataframe
    """
    def __init__(self):
        try:
            # Initialize the MongoDB client
            self.mongo_client = MongoDBClient()
            logging.info("MongoDB client initialized in USvisaData")
        except Exception as e:
            raise USvisaException(e, sys)

    def export_collection_as_dataframe(self, collection_name, database_name=None) -> pd.DataFrame:
        try:
            # Use the database from the mongo_client or the provided database_name
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client.client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns:
                df = df.drop("_id", axis=1)

            logging.info(f"Exported collection: {collection_name} as dataframe")
            return df
        except Exception as e:
            raise USvisaException(e, sys)